import cv2
import numpy as np
import time

# Image size (simulate your FPGA output resolution)
width = 64
height = 64

# Create an empty black image
image = np.zeros((height, width), dtype=np.uint8)

cv2.namedWindow("Simulated Image Receive", cv2.WINDOW_NORMAL)

# Simulate receiving pixel values one by one
for index in range(width * height):
    row = index // width
    col = index % width

    # Simulate a pixel value (just for demo, we use a gradient)
    pixel_value = int((index / (width * height)) * 255)

    image[row, col] = pixel_value

    # Optional: update display every few pixels for speed
    if index % 64 == 0 or index == (width * height - 1):
        cv2.imshow("Simulated Image Receive", image)
        cv2.waitKey(1)  # Required for OpenCV to update the window
        time.sleep(0.01)  # Slow it down to simulate data coming in

print("Image fill simulation complete.")
cv2.waitKey(0)
cv2.destroyAllWindows()
