import re
import glob

# 1. Fix the dropdown margin issue by removing margin-top and padding-top instead
with open('style.css', 'r') as f: css = f.read()
css = css.replace('margin-top: 15px;', 'top: calc(100% + 5px);') 
# Also remove the physical gap using a pseudo element or padding
css += """
.nav-dropdown::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    height: 20px;
}
.btn-group-standard {
    display: flex;
    gap: 15px;
    justify-content: flex-start;
    margin-top: 2rem;
    flex-wrap: wrap;
}
.btn-group-center {
    justify-content: center;
}
.btn-std {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    min-width: 160px;
    padding: 14px 24px;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 4px;
    transition: all 0.3s ease;
    text-decoration: none;
    cursor: pointer;
}
.btn-std-wholesale {
    background-color: var(--primary);
    color: var(--charcoal);
    border: 1px solid var(--primary);
}
.btn-std-wholesale:hover {
    background-color: var(--primary-hover);
}
.btn-std-retail {
    background-color: var(--charcoal);
    color: var(--gold);
    border: 1px solid var(--gold);
}
.btn-std-retail:hover {
    background-color: var(--gold);
    color: var(--charcoal);
}
.btn-std-fb {
    background-color: #1877F2;
    color: white;
    border: 1px solid #1877F2;
}
.btn-std-fb:hover {
    background-color: #166FE5;
}
"""
with open('style.css', 'w') as f: f.write(css)

button_html_start = """<div class="btn-group-standard fade-in-up" style="transition-delay: 0.2s;">
                    <a href="https://wa.me/6587593091" target="_blank" class="btn-std btn-std-wholesale">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg> Wholesale
                    </a>
                    <a href="https://order.fongfinest.com" target="_blank" class="btn-std btn-std-retail">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg> Retail
                    </a>
                    <a href="https://www.facebook.com/share/1DrzeiNQV6/" target="_blank" class="btn-std btn-std-fb">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg> Facebook
                    </a>
                </div>"""
                
button_html_center = button_html_start.replace('btn-group-standard', 'btn-group-standard btn-group-center')

# Update index.html
with open('index.html', 'r') as f: html = f.read()
html = re.sub(r'<div style="display: flex; gap: 15px; justify-content: flex-start; margin-top: 2rem;" class="fade-in-up" style="transition-delay: 0.2s;">.*?</div>', button_html_start, html, flags=re.DOTALL)
with open('index.html', 'w') as f: f.write(html)

# Update p/truffles.html
with open('p/truffles.html', 'r') as f: html = f.read()
# Replace footer buttons
html = re.sub(r'<div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;" class="mt-4">.*?</a>\s*</div>', button_html_center, html, flags=re.DOTALL)
# Also change the logo in the dropdown to black!
html = html.replace('assets/shoyu/logo.png', 'assets/shoyu/logo_black.png')
with open('p/truffles.html', 'w') as f: f.write(html)

# Do the dropdown logo change across all files
for fp in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(fp, 'r') as f: h = f.read()
    h = h.replace('assets/shoyu/logo.png', 'assets/shoyu/logo_black.png')
    with open(fp, 'w') as f: f.write(h)

