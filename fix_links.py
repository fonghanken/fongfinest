import re
import os

# Update index.html
with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('href="butter.html"', 'href="p/butter.html"')
content = content.replace('href="shoyu.html"', 'href="p/shoyu.html"')
content = content.replace('href="truffles.html"', 'href="p/truffles.html"')

with open('index.html', 'w') as f:
    f.write(content)

# Update individual pages
for file in ['p/butter.html', 'p/shoyu.html', 'p/truffles.html']:
    with open(file, 'r') as f:
        page = f.read()
    
    # style.css -> ../style.css
    page = page.replace('href="style.css"', 'href="../style.css"')
    # script.js -> ../script.js
    page = page.replace('src="script.js"', 'src="../script.js"')
    # index.html -> ../index.html
    page = page.replace('href="index.html', 'href="../index.html')
    # assets/ -> ../assets/
    page = page.replace('src="assets/', 'src="../assets/')
    page = page.replace("url('assets/", "url('../assets/")
    page = page.replace('href="assets/', 'href="../assets/')
    
    with open(file, 'w') as f:
        f.write(page)
