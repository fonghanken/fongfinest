import glob
for file in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(file, 'r') as f: html = f.read()
    html = html.replace('<div class="nav-actions" style="display: flex; gap: 10px;">', '<div class="nav-actions">')
    with open(file, 'w') as f: f.write(html)

with open('style.css', 'r') as f: css = f.read()
css_addition = """
.nav-actions {
    display: flex;
    gap: 10px;
}
"""
if '.nav-actions {' not in css:
    css = css.replace('.mobile-menu-toggle {', css_addition + '\n.mobile-menu-toggle {')
    with open('style.css', 'w') as f: f.write(css)
