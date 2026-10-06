from PIL import Image, ImageDraw

# Open the original image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")

# Determine the size for a perfect square
size = max(img.width, img.height)
# Add some padding so the logo doesn't touch the edge
padding = 30
base_size = size + padding * 2
scale = 4
hq_size = base_size * scale

# Create a transparent high-res background
bg_hq = Image.new('RGBA', (hq_size, hq_size), (0, 0, 0, 0))

# Draw a high-res white circle
draw = ImageDraw.Draw(bg_hq)
draw.ellipse((0, 0, hq_size, hq_size), fill=(255, 255, 255, 255))

# Resize background down to get smooth anti-aliased edges
bg = bg_hq.resize((base_size, base_size), Image.LANCZOS)

# Calculate position to paste the logo in the center
offset_x = (base_size - img.width) // 2
offset_y = (base_size - img.height) // 2

# Paste the logo using its alpha channel as the mask
bg.paste(img, (offset_x, offset_y), img)

# Save the result
bg.save('assets/truffles/logo.png')
print("Saved smooth white circle background logo.")
