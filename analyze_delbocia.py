from PIL import Image
import sys

img = Image.open('assets/butter/logo.webp').convert('RGBA')
width, height = img.size
print(f"Size: {width}x{height}")

# Find bounding box of non-transparent pixels
bbox = img.getbbox()
print(f"Content bbox: {bbox}")

# If we want a circle, the bounding box of the circle must be a square.
# Let's check the left side of the image.
# We can find the leftmost column that has content, and assume the circle extends to the right by `height` pixels?
# Let's print out some row/column density to understand where the shapes are.

cols = [0] * width
for x in range(width):
    for y in range(height):
        r, g, b, a = img.getpixel((x, y))
        # Assuming white is background, or transparent is background
        if a > 10 and not (r > 240 and g > 240 and b > 240):
            cols[x] += 1

# Print density in chunks
chunk_size = width // 20
if chunk_size == 0: chunk_size = 1
print("Column density (non-white/transparent pixels):")
for i in range(0, width, chunk_size):
    chunk = cols[i:i+chunk_size]
    print(f"Cols {i}-{i+chunk_size}: sum={sum(chunk)}")

