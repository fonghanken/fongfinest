from PIL import Image
img = Image.open('/Users/hanken/Desktop/fongenterprise/6_Media_Library/logo_f_black.png').convert("RGBA")
# Stretch to a perfect square
img_sq = img.resize((278, 278), Image.LANCZOS)
img_sq.save('assets/truffles/logo.png')
print("Saved stretched square logo.")
