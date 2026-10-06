from PIL import Image
import numpy as np

img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
arr = np.array(img)

# Find pixels that are dark (e.g. R, G, B all < 50) AND not fully transparent
# The black ring should be solid black or dark grey.
mask = (arr[:, :, 0] < 50) & (arr[:, :, 1] < 50) & (arr[:, :, 2] < 50) & (arr[:, :, 3] > 200)

y_indices, x_indices = np.where(mask)

if len(x_indices) > 0:
    min_x, max_x = x_indices.min(), x_indices.max()
    min_y, max_y = y_indices.min(), y_indices.max()
    print(f"Dark pixels bounding box: left={min_x}, right={max_x}, top={min_y}, bottom={max_y}")
    print(f"Width: {max_x - min_x}, Height: {max_y - min_y}")
    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    print(f"Center: ({center_x}, {center_y})")
    
    # Calculate radius of the ring
    radius = max((max_x - min_x), (max_y - min_y)) / 2
    print(f"Radius: {radius}")
else:
    print("No dark pixels found!")
