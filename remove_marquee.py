import re
with open('index.html', 'r') as f: html = f.read()

# Remove the marquee container block
html = re.sub(r'\s*<div class="marquee-container">.*?</div>\s*</div>', '', html, flags=re.DOTALL)

with open('index.html', 'w') as f: f.write(html)
