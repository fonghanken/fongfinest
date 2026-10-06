from PIL import Image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
pixels = img.load()
print(f"Center pixel: {pixels[133,139]}")
