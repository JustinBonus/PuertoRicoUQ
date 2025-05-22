import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import argparse

def load_elevation_data(filename):
    """Load elevation data from a space-delimited text file."""
    return np.loadtxt(filename)

def show_normal_image(data):
    """Show the elevation data as a grayscale image."""
    plt.imshow(data, cmap='gray')
    plt.colorbar(label='Elevation')
    plt.title('Elevation Map (Grayscale)')
    plt.show()

def show_hillshade(data, azdeg=315, altdeg=45):
    """Show a hillshade image of the elevation data."""
    ls = LightSource(azdeg=azdeg, altdeg=altdeg)
    hillshade = ls.shade(data, cmap=plt.cm.gray, vert_exag=1, blend_mode='overlay')
    plt.imshow(hillshade)
    plt.title('Hillshade Image')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Display elevation data as normal or hillshade image.')
    parser.add_argument('file', help='Path to the elevation data file')
    parser.add_argument('--mode', choices=['normal', 'hillshade'], default='normal', help='Display mode (normal or hillshade)')
    args = parser.parse_args()

    data = load_elevation_data(args.file)
    
    if args.mode == 'hillshade':
        show_hillshade(data)
    else:
        show_normal_image(data)

if __name__ == '__main__':
    main()
