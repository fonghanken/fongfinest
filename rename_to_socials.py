import glob

for fp in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(fp, 'r') as f: html = f.read()
    
    # 1. Replace the text inside the large CTA buttons
    # From </svg> Community  =>  </svg> Socials
    html = html.replace('</svg> Community\n', '</svg> Socials\n')
    html = html.replace('</svg> Community</a>', '</svg> Socials</a>')
    html = html.replace('</svg> Community </a>', '</svg> Socials </a>')
    
    # 2. Replace the navbar tooltip
    html = html.replace('data-tooltip="Community"', 'data-tooltip="Socials"')
    
    # 3. Replace floating action button aria-label
    html = html.replace('aria-label="Community"', 'aria-label="Socials"')
    
    with open(fp, 'w') as f: f.write(html)
    
print("Renamed Community to Socials")
