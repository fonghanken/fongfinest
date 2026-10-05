import os
import shutil
import re

gallery_dir = 'assets/shoyu/gallery'
source_dir = '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/shoyubros'

to_remove = [
    'BDP06300resized_5af231dc-05b0-4167-9db8-c96b5a664326_720x.jpg',
    'Mel_pic_2_720x.jpg'
]

to_add = [
    '321114160_1131935690855411_5292773682342895567_n.jpg',
    '327994268_1272801493268421_560928443823799637_n.jpg'
]

# 1. Remove the two identified images
for f in to_remove:
    path = os.path.join(gallery_dir, f)
    if os.path.exists(path):
        os.remove(path)

# 2. Add two new ones from desktop
for f in to_add:
    src = os.path.join(source_dir, f)
    dest = os.path.join(gallery_dir, f)
    shutil.copy(src, dest)

# 3. Read available images in gallery_dir
valid_images = sorted([f for f in os.listdir(gallery_dir) if f.endswith('.jpg') or f.endswith('.png')])

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

