from PIL import Image
import os
import math

gallery_dir = 'assets/shoyu/gallery'
attached_imgs = [
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791216912160.png',
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791216917982.png'
]

def image_diff(img1_path, img2_path):
    try:
        i1 = Image.open(img1_path).convert('RGB').resize((100, 100))
        i2 = Image.open(img2_path).convert('RGB').resize((100, 100))
        diff = 0
        for x in range(100):
            for y in range(100):
                p1 = i1.getpixel((x, y))
                p2 = i2.getpixel((x, y))
                diff += math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
        return diff
    except Exception as e:
        return float('inf')

for attached in attached_imgs:
    best_match = None
    min_diff = float('inf')
    for f in os.listdir(gallery_dir):
        if not f.endswith('.jpg') and not f.endswith('.png'): continue
        diff = image_diff(attached, os.path.join(gallery_dir, f))
        if diff < min_diff:
            min_diff = diff
            best_match = f
    print(f"Attached {os.path.basename(attached)} matches {best_match} (diff: {min_diff})")
