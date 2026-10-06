from PIL import Image, ImageDraw

# Open the original image
img = Image.open('assets/truffles/logo.png').convert("RGBA")

# Determine the size for a perfect square
size = max(img.width, img.height)
# Add some padding so the logo doesn't touch the edge
padding = 20
new_size = size + padding * 2

# Create a transparent background
bg = Image.new('RGBA', (new_size, new_size), (0, 0, 0, 0))

# Draw a white circle
draw = ImageDraw.Draw(bg)
draw.ellipse((0, 0, new_size, new_size), fill=(255, 255, 255, 255))

# Calculate position to paste the logo in the center
offset_x = (new_size - img.width) // 2
offset_y = (new_size - img.height) // 2

# Paste the logo using its alpha channel as the mask
bg.paste(img, (offset_x, offset_y), img)

# Save the result
bg.save('assets/truffles/logo.png')
print("Saved white circle background logo.")
