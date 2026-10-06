from PIL import Image, ImageDraw

img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
size = min(img.width, img.height)

# Center crop to a square
left = (img.width - size) / 2
top = (img.height - size) / 2
right = (img.width + size) / 2
bottom = (img.height + size) / 2
img_cropped = img.crop((left, top, right, bottom))

# Create a circular mask
mask = Image.new('L', (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

# Create a white background
bg = Image.new('RGBA', (size, size), (255, 255, 255, 255))

# Composite: Paste cropped image onto white background using the cropped image's alpha
bg.paste(img_cropped, (0, 0), img_cropped)

# Now, we want the OUTSIDE of the circle to be transparent.
# We apply the circular mask to the alpha channel of `bg`
final = Image.new('RGBA', (size, size), (0, 0, 0, 0))
final.paste(bg, (0, 0), mask)

# Save high quality
scale = 2
final_hq = final.resize((size * scale, size * scale), Image.LANCZOS)
final_hq.save('assets/truffles/logo.png')
print("Perfectly cropped to a circle.")
