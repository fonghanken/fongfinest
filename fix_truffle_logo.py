import re

with open('p/truffles.html', 'r') as f: html = f.read()

logo_html = '<img src="../assets/truffles/logo.png" alt="Brand Logo" style="max-height: 80px; margin: 0 auto 20px; display: block; opacity: 0.9;">'
html = re.sub(
    r'(<h2 class="section-title">Victorian Winter Truffle</h2>)',
    rf'{logo_html}\n                    \1',
    html
)

with open('p/truffles.html', 'w') as f: f.write(html)
