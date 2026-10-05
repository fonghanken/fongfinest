import glob

for file in glob.glob('p/*.html') + ['index.html']:
    with open(file, 'r') as f: html = f.read()
    html = html.replace('>Products</a>', '>Provisions</a>')
    html = html.replace('>About Us</a>', '>Our Story</a>')
    html = html.replace('>Contact</a>', '>Enquiry</a>')
    with open(file, 'w') as f: f.write(html)
