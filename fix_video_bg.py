import re

for file in ['p/shoyu.html', 'p/butter.html', 'p/truffles.html']:
    with open(file, 'r') as f:
        content = f.read()

    # Add background-image: none; to the hero section
    content = content.replace('background-color: #333;"', 'background-color: #333; background-image: none;"')

    # Fix poster and source paths if they don't start with ../ or http
    # poster="assets/...
    content = re.sub(r'poster="assets/', 'poster="../assets/', content)
    # src="assets/...
    content = re.sub(r'src="assets/([^"]+\.mp4)"', r'src="../assets/\1"', content)

    with open(file, 'w') as f:
        f.write(content)
