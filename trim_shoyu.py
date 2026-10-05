from PIL import Image

def trim_transparency(img):
    bbox = img.getbbox()
    if bbox:
        return img.crop(bbox)
    return img

try:
    img = Image.open('assets/shoyu/logo.png')
    img = img.convert("RGBA")
    trimmed = trim_transparency(img)
    trimmed.save('assets/shoyu/logo.png')
    print("Trimmed shoyu logo.")
except Exception as e:
    print("Error:", e)
