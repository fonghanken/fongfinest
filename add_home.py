import os
import glob

def add_home(filepath, is_subpage=False):
    with open(filepath, 'r') as f:
        html = f.read()
    
    target = '<a href="index.html#provisions"' if not is_subpage else '<a href="../index.html#provisions"'
    home_link = '<a href="index.html">Home</a>\n                ' if not is_subpage else '<a href="../index.html">Home</a>\n                '
    
    if target in html and '>Home<' not in html:
        html = html.replace(target, home_link + target)
        with open(filepath, 'w') as f:
            f.write(html)
        print(f"Added Home to {filepath}")

add_home('index.html', False)
for page in glob.glob('p/*.html'):
    add_home(page, True)
