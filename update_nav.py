import glob
import re

css = """
.nav-dropdown {
    position: relative;
    display: inline-block;
}
.nav-dropdown-content {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    background-color: var(--charcoal);
    min-width: 280px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.5);
    z-index: 100;
    border-radius: 8px;
    padding: 10px 0;
    margin-top: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.nav-dropdown:hover .nav-dropdown-content {
    display: block;
}
.nav-dropdown-item {
    padding: 12px 20px;
    display: flex !important;
    align-items: center;
    gap: 12px;
    color: var(--foreground) !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    font-family: var(--font-body) !important;
    white-space: nowrap;
    transition: background-color 0.2s !important;
}
.nav-dropdown-item::after {
    display: none !important;
}
.nav-dropdown-item:hover {
    background-color: var(--background);
}
.nav-dropdown-icon {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    object-fit: contain;
    background-color: white;
}
"""

with open('style.css', 'a') as f:
    f.write(css)

nav_actions_html = """            <div class="nav-actions">
                <a href="https://wa.me/6587593091" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-btn-icon" data-tooltip="Wholesale">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                </a>
                <a href="https://order.fongfinest.com" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-btn-icon" data-tooltip="Retail" style="background-color: var(--charcoal); color: var(--gold);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                </a>
                <a href="https://www.facebook.com/share/1DrzeiNQV6/" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-btn-icon" data-tooltip="Facebook" style="background-color: var(--charcoal); color: var(--gold);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </a>
            </div>"""

for filepath in glob.glob('*.html') + glob.glob('p/*.html'):
    with open(filepath, 'r') as f:
        html = f.read()

    prefix = "" if "/" not in filepath else "../"
    
    nav_links = f"""            <nav class="nav-links">
                <div class="nav-dropdown">
                    <a href="{prefix}index.html#portfolio" style="cursor: pointer;">Provisions</a>
                    <div class="nav-dropdown-content">
                        <a href="{prefix}p/truffles.html" class="nav-dropdown-item">
                            <img src="{prefix}assets/truffles/logo.png" alt="Ferrier Truffle" class="nav-dropdown-icon"> Ferrier Black Winter Truffle
                        </a>
                        <a href="{prefix}p/butter.html" class="nav-dropdown-item">
                            <img src="{prefix}assets/butter/logo.png" alt="Del Bocia" class="nav-dropdown-icon"> Del Bocia Heritage Butter
                        </a>
                        <a href="{prefix}p/shoyu.html" class="nav-dropdown-item">
                            <img src="{prefix}assets/shoyu/logo.png" alt="Shoyu Bros" class="nav-dropdown-icon"> Shoyu Bros Aged Shoyu
                        </a>
                    </div>
                </div>
                <a href="{prefix}index.html#provenance">Our Story</a>
                <a href="{prefix}index.html#contact">Enquiry</a>
            </nav>"""
            
    # Replace nav-links
    html = re.sub(r'            <nav class="nav-links">.*?</nav>', nav_links, html, flags=re.DOTALL)
    
    # Replace nav-actions
    html = re.sub(r'            <div class="nav-actions">.*?</div>', nav_actions_html, html, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(html)

print("Updated navbars across all files.")
