with open('index.html', 'r') as f: html = f.read()

# Replace "Products" with "Provisions" and reduce bottom margin
old_h2 = '<h2 class="section-title text-center fade-in-up" style="margin-bottom: 80px;">Products</h2>'
new_h2 = '<h2 class="section-title text-center fade-in-up" style="margin-bottom: 40px;">Provisions</h2>'
html = html.replace(old_h2, new_h2)

# Reduce top padding on the portfolio section
old_section = '<section id="portfolio" class="section portfolio-section rule-top">'
new_section = '<section id="portfolio" class="section portfolio-section rule-top" style="padding-top: 60px;">'
html = html.replace(old_section, new_section)

with open('index.html', 'w') as f: f.write(html)
