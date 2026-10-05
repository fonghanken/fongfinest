import os
import shutil
import re

uploaded_files = [
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791214839984.png',
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791214848666.png',
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791214863651.png',
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791214872104.png',
    '/Users/hanken/.gemini/antigravity/brain/17d2bd72-b311-4257-87d2-45a146a70d1d/.user_uploaded/media_1791214881551.png'
]

gallery_dir = 'assets/shoyu/gallery'

# Clear existing directory
for f in os.listdir(gallery_dir):
    os.remove(os.path.join(gallery_dir, f))

# Copy new files
img_tags = []
for i, src in enumerate(uploaded_files, start=1):
    ext = os.path.splitext(src)[1]
    new_name = f'roulette_{i}{ext}'
    dest = os.path.join(gallery_dir, new_name)
    shutil.copy(src, dest)
    img_tags.append(f'<img src="../assets/shoyu/gallery/{new_name}" alt="Shoyu Bros gallery image">')

# Create HTML block
inner_html = "\n                ".join(img_tags * 2) # Duplicate for infinite scroll
carousel_html = f'''
            <div class="infinite-carousel">
                {inner_html}
            </div>'''

# Update p/shoyu.html
with open('p/shoyu.html', 'r') as f:
    html = f.read()

# Replace the inner part of infinite-carousel-container
pattern = r'<div class="infinite-carousel">.*?</div>'
new_html = re.sub(pattern, carousel_html.strip(), html, flags=re.DOTALL)

with open('p/shoyu.html', 'w') as f:
    f.write(new_html)

