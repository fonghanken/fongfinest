import re

# 1. Update style.css
with open('style.css', 'r') as f:
    css = f.read()
css = css.replace('.value-prop-card {\n    background-color: #fff;', '.value-prop-card {\n    background-color: #fff;\n    color: var(--charcoal);')
with open('style.css', 'w') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()
html = html.replace('<div class="mt-10">', '<div style="margin-top: 80px;">')
with open('index.html', 'w') as f:
    f.write(html)
