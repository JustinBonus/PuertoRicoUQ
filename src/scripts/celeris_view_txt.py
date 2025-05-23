import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import argparse
import os

def load_elevation_data(filename):
    """Load elevation data from a space-delimited text file."""
    return np.loadtxt(filename)

def show_and_save_image(fig, filename):
    """Save and display the figure."""
    fig.savefig(filename, bbox_inches='tight')
    plt.show()

def show_normal_image(data, output_file):
    """Show and save the elevation data as a grayscale image."""
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='gray')
    fig.colorbar(cax, ax=ax, label='Elevation')
    ax.set_title('Elevation Map (Grayscale)')
    show_and_save_image(fig, output_file)

def show_hillshade(data, output_file, azdeg=315, altdeg=45):
    """Show and save a hillshade image of the elevation data."""
    ls = LightSource(azdeg=azdeg, altdeg=altdeg)
    hillshade = ls.shade(data, cmap=plt.cm.gray, vert_exag=1, blend_mode='overlay')
    
    fig, ax = plt.subplots()
    ax.imshow(hillshade)
    ax.set_title('Hillshade Image')
    show_and_save_image(fig, output_file)

def replace_extension_with_png(filename):
    """Replace file extension with .png"""
    base = os.path.splitext(filename)[0]
    return base + '.png'

def main():
    parser = argparse.ArgumentParser(description='Display and save elevation data as normal or hillshade image.')
    parser.add_argument('file', help='Path to the elevation data file')
    parser.add_argument('--mode', choices=['normal', 'hillshade'], default='normal', help='Display mode')
    args = parser.parse_args()

    data = load_elevation_data(args.file)
    output_file = replace_extension_with_png(args.file)

    if args.mode == 'hillshade':
        show_hillshade(data, output_file)
    else:
        show_normal_image(data, output_file)

if __name__ == '__main__':
    main()
