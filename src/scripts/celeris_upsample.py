import argparse
import numpy as np
from scipy.ndimage import zoom
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Upsample a 2D elevation dataset.")
    parser.add_argument("--input", required=True, help="Path to the input space-delimited text file.")
    parser.add_argument("--factor", type=float, required=True, help="Upsampling factor (e.g., 1.5, 2.0).")
    parser.add_argument("--type", choices=["nearest", "bilinear", "bicubic"], default="bilinear",
                        help="Interpolation method to use.")
    return parser.parse_args()

def get_order(interp_type):
    return {
        "nearest": 0,
        "bilinear": 1,
        "bicubic": 3,
    }[interp_type]

def main():
    args = parse_args()

    # Load the data
    data = np.loadtxt(args.input)

    # Determine interpolation order
    order = get_order(args.type)

    # Perform upsampling
    upsampled_data = zoom(data, zoom=args.factor, order=order)

    # Create output filename
    input_basename = os.path.splitext(os.path.basename(args.input))[0]
    output_filename = f"{input_basename}_upsample{args.factor}_{args.type}.txt"

    # Save to file
    np.savetxt(output_filename, upsampled_data, fmt="%.6f")

    print(f"Upsampled data saved to {output_filename}")

if __name__ == "__main__":
    main()
