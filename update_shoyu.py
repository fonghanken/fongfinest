import re

with open('p/shoyu.html', 'r') as f:
    content = f.read()

content = content.replace('<h1 class="hero-title">Heritage Artisanal Condiments</h1>', '<h1 class="hero-title">The Only Bro You\'ll Need.</h1>')
content = content.replace('<p class="hero-subtitle">Masterfully crafted flavors to elevate your culinary creations.</p>', '<p class="hero-subtitle">The magic shoyu that brings out the best in your dishes.</p>')

with open('p/shoyu.html', 'w') as f:
    f.write(content)
