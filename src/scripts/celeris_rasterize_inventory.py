import argparse
import sys
import pandas as pd
import numpy as np
from shapely import wkt
from shapely.geometry import box
import matplotlib.pyplot as plt
from shapely.affinity import translate

def main():
    # === Parse arguments ===
    parser = argparse.ArgumentParser(
        description="Rasterize building footprints from a CSV with geometry and number of floors."
    )
    parser.add_argument("-i", "--input", type=str, default="inventory.csv",
                        help="Input CSV file with geometry and NFloors columns (default: inventory.csv)")
    parser.add_argument("--dx", type=float, default=0.000009000009,
                        help="Pixel width in degrees (default: 0.000009000009)")
    parser.add_argument("--dy", type=float, default=0.000009000009,
                        help="Pixel height in degrees (default: 0.000009000009)")
    parser.add_argument("--floor_height", type=float, default=3.0,
                        help="Height per floor (default: 3.0)")

    try:
        args = parser.parse_args()
    except SystemExit:
        print("\n[ERROR] Invalid command line arguments.\n")
        print("Usage Example:")
        print("  python celeris_rasterize_inventory.py -i inventory.csv --dx 0.000009000009 --dy 0.000009000009 --floor_height 3.0\n")
        sys.exit(1)

    csv_file = args.input
    dx = args.dx
    dy = args.dy
    floor_height = args.floor_height

    # === Step 1: Load data ===
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {csv_file}")
        print("Please check the filename or provide a valid path using the -i or --input flag.")
        sys.exit(1)

    if 'geometry' not in df.columns or 'NFloors' not in df.columns:
        print("[ERROR] CSV file must contain 'geometry' and 'NFloors' columns.")
        sys.exit(1)

    df['NFloors'] = df['NFloors'].fillna(1).astype(int)
    df['geometry'] = df['geometry'].apply(wkt.loads)

    # === Step 2: Determine bounds ===
    all_bounds = [geom.bounds for geom in df['geometry']]
    minx = min(b[0] for b in all_bounds)
    miny = min(b[1] for b in all_bounds)
    maxx = max(b[2] for b in all_bounds)
    maxy = max(b[3] for b in all_bounds)

    width = int((maxx - minx) / dx) + 1
    height = int((maxy - miny) / dy) + 1
    print(f"Raster size: {width} x {height}")

    # === Step 3: Create raster and fill ===
    raster = np.zeros((height, width), dtype=np.uint8)

    for _, row in df.iterrows():
        poly = row['geometry']
        floors = row['NFloors']
        translated = translate(poly, xoff=-minx, yoff=-miny)

        min_col = int(translated.bounds[0] / dx)
        min_row = int(translated.bounds[1] / dy)
        max_col = int(translated.bounds[2] / dx)
        max_row = int(translated.bounds[3] / dy)

        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                pixel = box(j * dx, i * dy, (j + 1) * dx, (i + 1) * dy)
                if translated.intersects(pixel):
                    raster[height - i - 1, j] = max(raster[height - i - 1, j], int(floors * floor_height))

    # === Step 4: Display ===
    plt.figure(figsize=(10, 10))
    plt.imshow(raster, cmap='viridis', origin='upper')
    plt.colorbar(label='Height')
    plt.title("Building Footprint Raster")
    plt.xlabel("X pixels")
    plt.ylabel("Y pixels")

    # === Step 5: Save raster ===
    output_txt = csv_file.replace('.csv', '.txt')
    np.savetxt(output_txt, raster, fmt='%d', delimiter=' ')
    print(f"Raster saved to {output_txt} (shape: {raster.shape})")

    # === Step 6: Save raster as image ===
    output_img = output_txt.replace('.txt', '.png')
    plt.imsave(output_img, raster, cmap='viridis')
    print(f"Raster image saved to {output_img}")

if __name__ == "__main__":
    main()
