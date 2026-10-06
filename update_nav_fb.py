import glob
import re

old_fb_style = 'style="background-color: var(--charcoal); color: var(--gold);"'
new_fb_style = 'style="background-color: #1877F2; color: white; border-color: #1877F2;"'

for fp in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(fp, 'r') as f: html = f.read()
    
    # We want to replace it only for the Facebook button in the nav-actions
    # The string to look for:
    # <a href="https://www.facebook.com/share/1DrzeiNQV6/" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-btn-icon" data-tooltip="Facebook" style="background-color: var(--charcoal); color: var(--gold);">
    
    html = html.replace(
        '<a href="https://www.facebook.com/share/1DrzeiNQV6/" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-btn-icon" data-tooltip="Facebook" style="background-color: var(--charcoal); color: var(--gold);">',
        '<a href="https://www.facebook.com/share/1DrzeiNQV6/" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-btn-icon" data-tooltip="Facebook" style="background-color: #1877F2; color: white; border-color: #1877F2;">'
    )
    
    with open(fp, 'w') as f: f.write(html)
    
print("Updated Facebook button color in navbar")
