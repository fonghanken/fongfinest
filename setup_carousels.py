import os
import shutil

src_dirs = {
    'butter': '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/delbocia_files',
    'truffles': '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/truffles',
    'shoyu': '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/shoyubros'
}

dest_base = 'assets'

def get_image_files(d):
    try:
        return [f for f in os.listdir(d) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    except Exception as e:
        print(f"Error reading {d}: {e}")
        return []

html_snippets = {}

for product, src in src_dirs.items():
    dest_dir = os.path.join(dest_base, product, 'gallery')
    os.makedirs(dest_dir, exist_ok=True)
    
    files = get_image_files(src)
    # Take up to 10 images
    files = files[:10]
    
    img_tags = []
    for f in files:
        src_path = os.path.join(src, f)
        dest_path = os.path.join(dest_dir, f)
        shutil.copy2(src_path, dest_path)
        img_tags.append(f'<img src="../assets/{product}/gallery/{f}" alt="{product} gallery image">')
    
    # We need to duplicate the tags for seamless scrolling
    if img_tags:
        inner_html = "\n            ".join(img_tags * 2)
        carousel_html = f'''
        <div class="infinite-carousel-container fade-in-up">
            <div class="infinite-carousel">
                {inner_html}
            </div>
        </div>
        '''
        html_snippets[product] = carousel_html

# Now replace the existing grid galleries in the p/*.html files
import re

for file in ['p/shoyu.html', 'p/butter.html', 'p/truffles.html']:
    product = file.replace('p/', '').replace('.html', '')
    if product in html_snippets:
        with open(file, 'r') as f:
            content = f.read()
        
        # The existing gallery is typically a grid with a margin of 40px
        # We can look for <div style="margin: 40px 0; display: grid; ..."> ... </div>
        # Actually, let's just find the generic pattern for the old grid gallery:
        gallery_pattern = r'<div style="margin: 40px 0; display: grid; grid-template-columns: repeat\(auto-fit, minmax\(200px, 1fr\)\); gap: 20px;">.*?</div>'
        
        if re.search(gallery_pattern, content, flags=re.DOTALL):
            content = re.sub(gallery_pattern, html_snippets[product], content, flags=re.DOTALL)
        else:
            # If we couldn't find the grid, maybe insert it before the button row
            btn_pattern = r'(<div style="display: flex; justify-content: center; gap: 15px; margin-top: 30px; flex-wrap: wrap;">)'
            content = re.sub(btn_pattern, html_snippets[product] + r'\n\n                    \1', content)
        
        with open(file, 'w') as f:
            f.write(content)

