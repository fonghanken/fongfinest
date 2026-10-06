import glob

old_nav_wholesale = 'class="btn btn-primary nav-btn-icon" data-tooltip="Wholesale"'
new_nav_wholesale = 'class="btn btn-primary nav-btn-icon" data-tooltip="Wholesale" style="background-color: #25D366; color: white; border-color: #25D366;"'

for fp in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(fp, 'r') as f: html = f.read()
    html = html.replace(old_nav_wholesale, new_nav_wholesale)
    with open(fp, 'w') as f: f.write(html)
    
print("Updated nav wholesale color")
