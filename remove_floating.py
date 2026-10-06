import re
import glob

for fp in ['p/butter.html', 'p/shoyu.html', 'p/truffles.html']:
    with open(fp, 'r') as f: html = f.read()
    
    # Remove the floating action block entirely
    html = re.sub(r'<!-- Floating Action Buttons -->.*?</div>\s*<script', '<script', html, flags=re.DOTALL)
    
    with open(fp, 'w') as f: f.write(html)
    
print("Removed floating buttons.")
