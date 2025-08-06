from PIL import Image

# Load and convert image
img = Image.open("lena.png").convert("L")
img.save("Grey lana.png")
img.show()  # Optional: show the image