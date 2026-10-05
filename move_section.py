import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Extract the Value Prop block (including title "Provisions the way they should be")
vp_pattern = r'(<div style="margin-top: 80px;">\s*<h2 class="section-title text-center fade-in-up">Provisions the way they should be\.</h2>\s*<div class="grid mt-6".*?</div>\s*</div>)'
match = re.search(vp_pattern, html, flags=re.DOTALL)

if match:
    vp_block = match.group(1)
    # Remove from old location
    html = html.replace(vp_block, '')
    
    # Remove the <div style="margin-top: 80px;"> wrapper from vp_block to integrate cleanly
    vp_inner = re.sub(r'^<div style="margin-top: 80px;">\s*', '', vp_block)
    vp_inner = re.sub(r'\s*</div>$', '', vp_inner)
    
    # Optional: Change h2 to h3 since Purveyors is the h2
    vp_inner = vp_inner.replace('<h2 class="section-title text-center fade-in-up">', '<h3 class="section-title text-center fade-in-up" style="margin-top: 60px;">')
    vp_inner = vp_inner.replace('</h2>', '</h3>')

    # 2. Replace advantage-grid in provenance
    adv_pattern = r'<div class="grid advantage-grid mt-6">.*?</div>\s*</div>\s*</div>\s*</section>'
    adv_match = re.search(adv_pattern, html, flags=re.DOTALL)
    if adv_match:
        # We just want to replace the div.grid advantage-grid, but regex is tricky. Let's do it safely.
        pass

# Safe replacement for advantage grid
adv_grid_pattern = r'<div class="grid advantage-grid mt-6">.*?<span class="advantage-number">03</span>.*?</div>\s*</div>'
html = re.sub(adv_grid_pattern, vp_inner, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
