from PIL import Image, ImageDraw

# Open original image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")

# Crop to the exact bounds of the black ring
ring_box = (15, 10, 260, 262)
img_cropped = img.crop(ring_box)

# Stretch to a perfect square (the ring becomes a perfect circle)
# Use a high-res base for smoothness
base_size = max(img_cropped.width, img_cropped.height)
scale = 4
hr_size = base_size * scale

img_hr = img_cropped.resize((hr_size, hr_size), Image.LANCZOS)

# Create white circle background
bg = Image.new('RGBA', (hr_size, hr_size), (0, 0, 0, 0))
draw = ImageDraw.Draw(bg)
draw.ellipse((0, 0, hr_size, hr_size), fill=(255, 255, 255, 255))

# Paste the stretched ring onto the white circle
bg.paste(img_hr, (0, 0), img_hr)

# Optional: Apply a strict circular mask to clean the outside edges completely
mask = Image.new('L', (hr_size, hr_size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, hr_size, hr_size), fill=255)

final_bg = Image.new('RGBA', (hr_size, hr_size), (0, 0, 0, 0))
final_bg.paste(bg, (0, 0), mask)

# Resize down for perfect anti-aliasing
final = final_bg.resize((base_size, base_size), Image.LANCZOS)
final.save('assets/truffles/logo.png')
print("Saved perfectly centered, stretched, and masked circular logo.")
