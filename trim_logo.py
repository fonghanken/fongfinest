from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

try:
    im = Image.open('assets/shoyu/logo.png')
    trimmed_im = trim(im)
    trimmed_im.save('assets/shoyu/logo.png')
    print("Trimmed shoyu logo.")
except Exception as e:
    print("Error trimming shoyu logo:", e)

# Just in case, trim Delbocia too? 
try:
    im2 = Image.open('assets/butter/logo.png')
    trimmed_im2 = trim(im2)
    trimmed_im2.save('assets/butter/logo.png')
    print("Trimmed butter logo.")
except Exception as e:
    print("Error trimming butter logo:", e)
