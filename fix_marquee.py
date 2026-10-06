import re
with open('index.html', 'r') as f: html = f.read()

marquee_block = """        <div class="marquee-container">
                <div class="marquee-content">
                    EXCLUSIVE DISTRIBUTORS &nbsp;⭑&nbsp; DIRECT IMPORT &nbsp;⭑&nbsp; RESTAURANT QUALITY &nbsp;⭑&nbsp; 100% ARTISANAL &nbsp;⭑&nbsp; FAMILY HERITAGE &nbsp;⭑&nbsp; EXCLUSIVE DISTRIBUTORS &nbsp;⭑&nbsp; DIRECT IMPORT &nbsp;⭑&nbsp; RESTAURANT QUALITY &nbsp;⭑&nbsp; 100% ARTISANAL &nbsp;⭑&nbsp; FAMILY HERITAGE &nbsp;⭑&nbsp;
                </div>
            </div>"""

# Remove the old main-overlap and marquee block
html = re.sub(r'\s*<div class="main-overlap">\s*<div class="marquee-container">.*?</div>\s*</div>\s*', '\n        ', html, flags=re.DOTALL)
html = re.sub(r'\s*<div class="main-overlap">\s*<div class="marquee-container">.*?</div>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'\s*<div class="main-overlap">\s*<div class="marquee-container">.*?</div>\s*', '\n        ', html, flags=re.DOTALL)

# Insert the marquee right before the about section
html = html.replace('<section id="about"', f'{marquee_block}\n        <section id="about"')

with open('index.html', 'w') as f: f.write(html)
