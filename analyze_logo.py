from PIL import Image
import numpy as np

img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
arr = np.array(img)

# Find all pixels with alpha > 10
y_indices, x_indices = np.where(arr[:, :, 3] > 10)

min_x, max_x = x_indices.min(), x_indices.max()
min_y, max_y = y_indices.min(), y_indices.max()

print(f"Bounding box: left={min_x}, right={max_x}, top={min_y}, bottom={max_y}")
print(f"Width: {max_x - min_x}, Height: {max_y - min_y}")
