from PIL import Image, ImageDraw

# Open the original image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")

# We want a high-res output for smoothness
scale = 4
orig_w, orig_h = img.size
max_dim = max(orig_w, orig_h)
# Give it a little bit of padding so the ring isn't touching the edge
pad = 10
sq_size = max_dim + pad * 2

# Scale everything up
hr_size = sq_size * scale
img_hr = img.resize((orig_w * scale, orig_h * scale), Image.LANCZOS)

# Create a transparent background
bg = Image.new('RGBA', (hr_size, hr_size), (0, 0, 0, 0))

# The black ring in the original image is an ellipse/circle.
# Let's just draw a white circle that is slightly smaller than the bounding box
# to make sure it doesn't peek out of the black ring, OR exactly the size of the ring!
# Since the black ring is 266x278, let's draw a white ellipse of that size.
draw = ImageDraw.Draw(bg)
ellipse_x = pad * scale
ellipse_y = pad * scale
ellipse_w = orig_w * scale
ellipse_h = orig_h * scale
draw.ellipse((ellipse_x, ellipse_y, ellipse_x + ellipse_w, ellipse_y + ellipse_h), fill=(255, 255, 255, 255))

# Paste the image on top of the white ellipse
offset_x = pad * scale
offset_y = pad * scale
bg.paste(img_hr, (offset_x, offset_y), img_hr)

# Resize down for anti-aliasing
final = bg.resize((sq_size, sq_size), Image.LANCZOS)
final.save('assets/truffles/logo.png')
print("Perfect white background applied inside the ring bounds.")
