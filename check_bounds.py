from PIL import Image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
bbox = img.getbbox()
print(f"Image size: {img.size}")
print(f"Bounding box of non-transparent content: {bbox}")
