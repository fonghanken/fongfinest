import os
import shutil
import re

gallery_dir = 'assets/shoyu/gallery'
new_img_src = '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791214932613.png'

# 1. Delete roulette_1 and roulette_2
for f in ['roulette_1.png', 'roulette_2.png']:
    try:
        os.remove(os.path.join(gallery_dir, f))
    except:
        pass

# 2. Copy the new image as roulette_6.png
shutil.copy(new_img_src, os.path.join(gallery_dir, 'roulette_6.png'))

# 3. Read available images in gallery_dir
valid_images = sorted([f for f in os.listdir(gallery_dir) if f.endswith('.png')])

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

