import re
import os
import shutil
import glob

# 1. Butter & Truffle Hero Text
with open('p/butter.html', 'r') as f: butter = f.read()
butter = re.sub(r'<h1 class="hero-title.*?</h1>', r'<h1 class="hero-title fade-in-up" style="color: var(--cream); font-size: 3.5rem;">A Butter Not For Ordinary People</h1>', butter, count=1)
butter = re.sub(r'<p class="hero-subtitle.*?</p>', r'<p class="hero-subtitle fade-in-up" style="color: var(--gold); transition-delay: 0.1s;">Consecutively crowned for unmatched quality: pure, preservative-free butter crafted with history and heart.</p>', butter, count=1)
with open('p/butter.html', 'w') as f: f.write(butter)

with open('p/truffles.html', 'r') as f: truffles = f.read()
truffles = re.sub(r'<h1 class="hero-title.*?</h1>', r'<h1 class="hero-title fade-in-up" style="color: var(--cream); font-size: 3.5rem;">Unearthed with Care. Revered by Chefs</h1>', truffles, count=1)
truffles = re.sub(r'<p class="hero-subtitle.*?</p>', r'<p class="hero-subtitle fade-in-up" style="color: var(--gold); transition-delay: 0.1s;">Aromatic black winter truffles sustainably grown, hand-harvested, and crafted for extraordinary culinary experiences.</p>', truffles, count=1)
with open('p/truffles.html', 'w') as f: f.write(truffles)

# 2. Instagram Contrast
for file in ['p/shoyu.html', 'p/butter.html', 'p/truffles.html']:
    with open(file, 'r') as f: html = f.read()
    html = html.replace('background-color: var(--vintage-black, #1a1a1a); border-color: var(--vintage-black, #1a1a1a);',
                        'background-color: var(--vintage-black, #1a1a1a); border-color: var(--vintage-black, #1a1a1a); color: var(--cream);')
    with open(file, 'w') as f: f.write(html)

# 3. Wholesale/Retail Buttons safely
wholesale_new = '''<a href="https://wa.me/6587593091" target="_blank" rel="noopener noreferrer" class="btn" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.95rem; padding: 12px 24px; background-color: #25D366; color: white; border: none; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
                    WHOLESALE
                </a>'''

retail_new = '''<a href="https://order.fongfinest.com" target="_blank" rel="noopener noreferrer" class="btn" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.95rem; padding: 12px 24px; background-color: var(--cream, #f9f8f4); color: var(--charcoal, #1a2b27); border: none; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                    RETAIL
                </a>'''

for file in glob.glob('p/*.html') + ['index.html']:
    with open(file, 'r') as f: html = f.read()
    # Replace line by line matching the hrefs to avoid DOTALL issues
    
    # Simple wholesale match (the <a... wholesale </a>)
    # They usually look like: <a href="https://wa.me/6587593091"...>Wholesale</a>
    # We will use re.sub without DOTALL, so it only matches if it's on the same line or we can just replace the specific strings.
    # Actually, they span multiple lines! Let's write a safe regex using non-greedy that doesn't use .*? across tags.
    html = re.sub(r'<a[^>]*href="https://wa.me/6587593091"[^>]*>.*?Wholesale.*?</a>', wholesale_new, html, flags=re.IGNORECASE | re.DOTALL)
    # Wait! .*? still risks matching across multiple tags if Wholesale isn't inside that specific tag!
    # Let's be safer: match only spaces or newlines inside the tag.
    html = re.sub(r'<a[^>]*href="https://wa.me/6587593091"[^>]*>[\s\n]*Wholesale[\s\n]*</a>', wholesale_new, html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<a[^>]*href="https://wa.me/6587593091"[^>]*>[\s\n]*<svg.*?</svg>[\s\n]*Wholesale[\s\n]*</a>', wholesale_new, html, flags=re.IGNORECASE | re.DOTALL)
    
    html = re.sub(r'<a[^>]*href="https://order.fongfinest.com"[^>]*>[\s\n]*Retail[\s\n]*</a>', retail_new, html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<a[^>]*href="https://order.fongfinest.com"[^>]*>[\s\n]*<svg.*?</svg>[\s\n]*Retail[\s\n]*</a>', retail_new, html, flags=re.IGNORECASE | re.DOTALL)
    
    with open(file, 'w') as f: f.write(html)

# 4. Logos next to titles in index.html
with open('index.html', 'r') as f: html = f.read()
truffle_logo = '<img src="assets/truffles/logo.png" style="height: 1.6rem; width: auto; object-fit: contain; border-radius: 50%;">'
html = html.replace('Victorian Winter Truffle</h3>', f'<span style="display: flex; align-items: center; gap: 10px;">{truffle_logo} Victorian Winter Truffle</span></h3>')

butter_logo = '<img src="assets/butter/logo.webp" style="height: 1.6rem; width: auto; object-fit: contain; border-radius: 50%;">'
html = html.replace('Del Bocia Heritage Butter</h3>', f'<span style="display: flex; align-items: center; gap: 10px;">{butter_logo} Del Bocia Heritage Butter</span></h3>')

shoyu_logo = '<img src="assets/shoyu/logo.png" style="height: 1.6rem; width: auto; object-fit: contain;">'
html = html.replace('Shoyu Bros Aged Shoyu</h3>', f'<span style="display: flex; align-items: center; gap: 10px;">{shoyu_logo} Shoyu Bros Aged Shoyu</span></h3>')
with open('index.html', 'w') as f: f.write(html)

# 5. Shoyu Carousel Fix
gallery_dir = 'assets/shoyu/gallery'
urls = [
    'https://shoyubros.com/cdn/shop/files/BDP06300resized_5af231dc-05b0-4167-9db8-c96b5a664326_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/IMG_20210123_085541_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/IMG_20210123_090956_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/IMG_5739_720x.jpg',
    'https://shoyubros.com/cdn/shop/files/Mel_pic_2_720x.jpg'
]
local_src = '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/shoyubros'
os.system(f"rm -rf {gallery_dir}/*")
os.system(f"cd {gallery_dir} && curl -s -O {urls[0]} -O {urls[1]} -O {urls[2]} -O {urls[3]} -O {urls[4]}")
local_files = [f for f in os.listdir(local_src) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
for f in local_files[:10]:
    shutil.copy(os.path.join(local_src, f), os.path.join(gallery_dir, f))

valid_images = sorted([f for f in os.listdir(gallery_dir) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.webp')])
img_tags = [f'<img src="../assets/shoyu/gallery/{img}" alt="Shoyu Bros gallery image">' for img in valid_images]
carousel_html = f'<div class="infinite-carousel">\n                ' + "\n                ".join(img_tags * 2) + '\n            </div>'

with open('p/shoyu.html', 'r') as f: html = f.read()
html = re.sub(r'<div class="infinite-carousel">.*?</div>', carousel_html, html, flags=re.DOTALL)
with open('p/shoyu.html', 'w') as f: f.write(html)

print("Done with all python fixes!")
