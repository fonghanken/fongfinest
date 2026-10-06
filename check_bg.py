from PIL import Image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
pixels = img.load()
print(f"Top-left corner pixel: {pixels[0,0]}")
print(f"Top-right corner pixel: {pixels[265,0]}")
