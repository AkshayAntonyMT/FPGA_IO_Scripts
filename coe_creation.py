from PIL import Image

# Load and convert image
img = Image.open("c:/Users/aksha/OneDrive/Desktop/Project/FPGA IO Scripts/lena_greyscale.png").convert("L")  # "L" mode = grayscale
pixels = list(img.getdata())

# Output COE file
with open("c:/Users/aksha/OneDrive/Desktop/Project/FPGA IO Scripts/lana.coe", "w") as f:
    f.write("memory_initialization_radix=16;\n")
    f.write("memory_initialization_vector=\n")

    for i, pixel in enumerate(pixels):
        hex_val = f"{pixel:02X}"
        if i != len(pixels) - 1:
            f.write(hex_val + ",\n")
        else:
            f.write(hex_val + ";\n")
