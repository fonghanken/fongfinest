import re

for file in ['p/shoyu.html', 'p/butter.html', 'p/truffles.html']:
    with open(file, 'r') as f:
        content = f.read()

    # Make the product section truly cream background with dark text
    # The section is: <section class="section about-section bg-cream">
    content = content.replace('<section class="section about-section bg-cream">', '<section class="section about-section" style="background-color: var(--cream); color: var(--charcoal);">')
    
    # Remove filter: brightness(0) from logos since background is now light
    content = content.replace('filter: brightness(0); opacity: 0.9;', 'opacity: 0.9;')
    
    with open(file, 'w') as f:
        f.write(content)
