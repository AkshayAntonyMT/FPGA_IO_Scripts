import numpy as np
from PIL import Image

# Load pixel values from text file
with open("inverted_lana.txt", "r") as f:
    pixels = [int(line.strip().rstrip(','), 16) for line in f]

# Define image dimensions (you must know this from original image)
width = 512
height = 512

# Check if the number of pixels is correct
assert len(pixels) == width * height, "Pixel count doesn't match image size"

# Convert to 2D array
pixel_array = np.array(pixels, dtype=np.uint8).reshape((height, width))

# Create and save image
img = Image.fromarray(pixel_array, mode='L')  # 'L' = 8-bit grayscale
img.save("inverted_output.png")
img.show()  # Optional: show the image
