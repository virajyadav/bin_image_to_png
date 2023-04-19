import numpy as np
import cv2

# Set the shape and data type of the raw image
width = 640
height = 480
shape = (height, width)
dtype = np.uint8  # data type of the image

# Load the raw image data from the .bin file
with open("raw_images.bin", "rb") as f:
    raw_data = np.fromfile(f, dtype=dtype)

# Calculate the expected size of each image
expected_size = width * height

# Iterate over each image in the raw data
for i in range(0, len(raw_data), expected_size):
    # Extract the raw image data for this image
    raw_image_data = raw_data[i:i+expected_size]

    # Reshape the raw image data to the specified shape if the sizes match
    if raw_image_data.size == expected_size:
        raw_image_data = raw_image_data.reshape(shape)
    else:
        print(f"Error: Input array size is {raw_image_data.size}, expected size is {expected_size}")
        continue

    # Convert the raw image to RGB using OpenCV
    rgb_image = cv2.cvtColor(raw_image_data, cv2.COLOR_BayerBG2RGB)

    # Write the RGB image to disk using OpenCV
    filename = f"image_{i//expected_size}.png"
    cv2.imwrite(filename, rgb_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
