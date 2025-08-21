import cv2

# Read image
img = cv2.imread("lena_greyscale.png")   # replace with your image path

# Resize to 64x64
resized_img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)

# Save output
cv2.imwrite("resized.png", resized_img)

# If you want to display
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
