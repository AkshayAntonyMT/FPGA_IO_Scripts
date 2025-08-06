import serial
import numpy as np
import cv2

# ======================= USER CONFIG ===========================
width = 512
height = 512
port = 'COM3'            # 🛠️ Replace with your actual COM port
baudrate = 115200        # 🛠️ Match with your FPGA UART baud rate
update_interval = 1024   # Update display every N pixels
# ===============================================================

# Open the serial port
ser = serial.Serial(port, baudrate, timeout=1)

# Prepare a black image buffer
image = np.zeros((height, width), dtype=np.uint8)
index = 0

# OpenCV display window
cv2.namedWindow("Receiving 512x512 Image", cv2.WINDOW_NORMAL)

print("Receiving image...")

while index < width * height:
    if ser.in_waiting:
        byte = ser.read()  # Read one byte
        pixel_value = int.from_bytes(byte, byteorder='big')

        # Compute row and column
        row = index // width
        col = index % width

        # Store pixel
        image[row, col] = pixel_value
        index += 1

        # Refresh window every few pixels for speed
        if index % update_interval == 0 or index == width * height:
            cv2.imshow("Receiving 512x512 Image", image)
            cv2.waitKey(1)

print("Image reception complete.")
cv2.imshow("Final Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
ser.close()
