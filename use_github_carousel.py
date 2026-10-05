import os
import re

gallery_dir = 'assets/shoyu/gallery'
urls = [
    'https://shoyubros.com/cdn/shop/files/BDP06300resized_5af231dc-05b0-4167-9db8-c96b5a664326_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/IMG_20210123_085541_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/IMG_20210123_090956_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/IMG_5739_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/Mel_pic_2_720x.jpg'
]

# 1. Clear out all existing gallery images (including roulette_6.png)
for f in os.listdir(gallery_dir):
    try:
        os.remove(os.path.join(gallery_dir, f))
    except:
        pass

# 2. Download the URLs
os.system(f"cd {gallery_dir} && curl -s -O {urls[0]} -O {urls[1]} -O {urls[2]} -O {urls[3]} -O {urls[4]}")

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

