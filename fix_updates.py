import re

# 1. Update individual product pages to revert background and invert logos
for file in ['p/shoyu.html', 'p/butter.html', 'p/truffles.html']:
    with open(file, 'r') as f:
        content = f.read()

    # Change background back to charcoal (green) and text to cream (foreground)
    content = content.replace('style="background-color: var(--cream); color: var(--charcoal);"', 'class="section about-section bg-cream" style="background-color: var(--charcoal); color: var(--foreground);"')
    content = content.replace('<section class="section about-section" class="section about-section bg-cream"', '<section class="section about-section bg-cream"')
    
    # Actually wait, if I did string replacement before, let's just make it robust:
    content = re.sub(r'<section class="section about-section"[^>]*>', '<section class="section about-section bg-cream">', content)
    
    # Invert logos so they are white (readable on green)
    content = content.replace('opacity: 0.9;', 'filter: brightness(0) invert(1); opacity: 0.9;')
    
    with open(file, 'w') as f:
        f.write(content)

# 2. Move Value Prop into About Us in index.html
with open('index.html', 'r') as f:
    idx_content = f.read()

# Extract Value prop section
vp_pattern = r'(<!-- Value Proposition Section -->\s*<section class="section">\s*<div class="container">\s*<h2 class="section-title text-center fade-in-up">Provisions the way they should be\.</h2>.*?</div>\s*</section>)'
match = re.search(vp_pattern, idx_content, flags=re.DOTALL)
if match:
    vp_html = match.group(1)
    
    # Remove from original location
    idx_content = idx_content.replace(vp_html, '')
    
    # The vp_html is a <section>. We want to move its inner content into the About Us container, or just place the whole block inside the about section?
    # Actually, placing a <section> inside a <section> is invalid HTML.
    # Let's extract the inner container or grid.
    grid_pattern = r'(<h2 class="section-title text-center fade-in-up">Provisions the way they should be\.</h2>\s*<div class="grid mt-6".*?</div>\s*</div>)'
    grid_match = re.search(grid_pattern, vp_html, flags=re.DOTALL)
    if grid_match:
        grid_html = grid_match.group(1)
        
        # Insert it inside About Us section, right after the text.
        about_pattern = r'(<p class="body-text mt-2">We guarantee pristine cold-chain freshness, authenticity, and outstanding flavour\. Elevate your creations with us today\.</p>\s*</div>)'
        
        replacement = r'\1\n\n                    <div class="mt-10">\n                        ' + grid_html.replace('\n', '\n                        ') + '\n                    </div>'
        idx_content = re.sub(about_pattern, replacement, idx_content)

with open('index.html', 'w') as f:
    f.write(idx_content)
