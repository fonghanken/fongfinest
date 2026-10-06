import glob

for fp in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(fp, 'r') as f: html = f.read()
    
    # 1. Replace the text inside the large CTA buttons
    # From </svg> Facebook  =>  </svg> Community
    html = html.replace('</svg> Facebook\n', '</svg> Community\n')
    html = html.replace('</svg> Facebook</a>', '</svg> Community</a>')
    html = html.replace('</svg> Facebook </a>', '</svg> Community </a>')
    
    # 2. Replace the navbar tooltip
    html = html.replace('data-tooltip="Facebook"', 'data-tooltip="Community"')
    
    # 3. Replace floating action button aria-label
    html = html.replace('aria-label="Facebook"', 'aria-label="Community"')
    
    with open(fp, 'w') as f: f.write(html)
    
print("Renamed Facebook to Community")
