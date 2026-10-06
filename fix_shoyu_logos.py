import re
import glob

for fp in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(fp, 'r') as f: html = f.read()
    
    # First revert ALL logo_black.png to logo.png
    html = html.replace('assets/shoyu/logo_black.png', 'assets/shoyu/logo.png')
    
    # Then selectively replace only the one inside nav-dropdown-item
    # It looks like: <img src="assets/shoyu/logo.png" alt="Shoyu Bros" class="nav-dropdown-icon">
    # or <img src="../assets/shoyu/logo.png" alt="Shoyu Bros" class="nav-dropdown-icon">
    
    html = html.replace('assets/shoyu/logo.png" alt="Shoyu Bros" class="nav-dropdown-icon"', 'assets/shoyu/logo_black.png" alt="Shoyu Bros" class="nav-dropdown-icon"')
    
    with open(fp, 'w') as f: f.write(html)

print("Fixed shoyu logos.")
