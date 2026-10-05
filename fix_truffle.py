from PIL import Image
import os
import math
import shutil
import re

attached = '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791217012290.jpg'
truffle_src = '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/truffles'

def image_diff(img1_path, img2_path):
    try:
        i1 = Image.open(img1_path).convert('RGB').resize((50, 50))
        i2 = Image.open(img2_path).convert('RGB').resize((50, 50))
        diff = 0
        for x in range(50):
            for y in range(50):
                p1 = i1.getpixel((x, y))
                p2 = i2.getpixel((x, y))
                diff += math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
        return diff
    except Exception as e:
        return float('inf')

bad_match = None
min_diff = float('inf')

for f in os.listdir(truffle_src):
    if not f.endswith('.jpg') and not f.endswith('.png'): continue
    diff = image_diff(attached, os.path.join(truffle_src, f))
    if diff < min_diff:
        min_diff = diff
        bad_match = f

print(f"Bad match found: {bad_match} (diff: {min_diff})")

# Let's rebuild the galleries to have exactly 15 images for each
products = {
    'butter': '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/delbocia_files',
    'truffles': '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/truffles',
    'shoyu': '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/shoyubros'
}

for product, src_dir in products.items():
    gallery_dir = f'assets/{product}/gallery'
    os.makedirs(gallery_dir, exist_ok=True)
    
    # clear existing
    for f in os.listdir(gallery_dir):
        os.remove(os.path.join(gallery_dir, f))
    
    # get valid files
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    
    # Exclude bad_match for truffles
    if product == 'truffles' and bad_match in files:
        files.remove(bad_match)
        
    # Pick 15 images (or as many as available up to 15)
    selected = files[:15]
    
    img_tags = []
    for f in selected:
        shutil.copy(os.path.join(src_dir, f), os.path.join(gallery_dir, f))
        img_tags.append(f'<img src="../assets/{product}/gallery/{f}" alt="{product} gallery image">')
        
    inner_html = "\n                ".join(img_tags * 2)
    carousel_html = f'''<div class="infinite-carousel">
                {inner_html}
            </div>'''
            
    html_file = f'p/{product}.html'
    with open(html_file, 'r') as f:
        html = f.read()
        
    pattern = r'<div class="infinite-carousel">.*?</div>'
    html = re.sub(pattern, carousel_html, html, flags=re.DOTALL)
    
    with open(html_file, 'w') as f:
        f.write(html)
        
print("Carousels updated to 15 images.")
