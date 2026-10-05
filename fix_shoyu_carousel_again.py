import os
import shutil
import re

gallery_dir = 'assets/shoyu/gallery'
source_dir = '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/shoyubros'

# High quality images from the desktop folder
high_quality_imgs = [
    '321114160_1131935690855411_5292773682342895567_n.jpg',
    '327994268_1272801493268421_560928443823799637_n.jpg',
    '328259021_6011536548884762_2778400187351916573_n.jpg',
    '480606343_659499283087762_9020050314125945503_n.jpg'
]

# 1. Clear out all existing gallery images EXCEPT roulette_6.png (the one they just uploaded)
for f in os.listdir(gallery_dir):
    if f != 'roulette_6.png':
        try:
            os.remove(os.path.join(gallery_dir, f))
        except:
            pass

# 2. Copy the high-quality ones into the gallery
for img in high_quality_imgs:
    src = os.path.join(source_dir, img)
    dest = os.path.join(gallery_dir, img)
    shutil.copy(src, dest)

# 3. Read available images in gallery_dir
valid_images = sorted([f for f in os.listdir(gallery_dir)])

# 4. Generate HTML img tags
img_tags = []
for img in valid_images:
    img_tags.append(f'<img src="../assets/shoyu/gallery/{img}" alt="Shoyu Bros gallery image">')

# 5. Duplicate tags for the infinite loop
inner_html = "\n                ".join(img_tags * 2)
carousel_html = f'''<div class="infinite-carousel">
                {inner_html}
            </div>'''

# 6. Replace in p/shoyu.html
with open('p/shoyu.html', 'r') as f:
    html = f.read()

pattern = r'<div class="infinite-carousel">.*?</div>'
new_html = re.sub(pattern, carousel_html, html, flags=re.DOTALL)

with open('p/shoyu.html', 'w') as f:
    f.write(new_html)

