import re

def update_page(filename, logo_url, poster_img):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Update Hero section to use video
    hero_pattern = r'<section class="hero fade-in-up" style="background-image: url\(([^)]+)\)[^>]*>[\s\S]*?<div class="hero-overlay"[^>]*></div>'
    
    video_html = f'''<section class="hero hero-video-container fade-in-up" style="position: relative; overflow: hidden; background-color: #333;">
        <video class="hero-video" autoplay loop muted playsinline poster="{poster_img}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6; z-index: 1;">
            <source src="assets/{filename.replace(".html", "")}-hero.mp4" type="video/mp4">
        </video>
        <div class="hero-overlay" style="background: rgba(0,0,0,0.4); position: absolute; inset: 0; z-index: 2;"></div>'''

    content = re.sub(hero_pattern, video_html, content)
    
    # 2. Add logo
    title_pattern = r'(<h2 class="section-title">.*?</h2>)'
    logo_html = f'<img src="{logo_url}" alt="Brand Logo" style="max-height: 80px; margin: 0 auto 20px; display: block;">\n                    \\1'
    if logo_url:
        content = re.sub(title_pattern, logo_html, content)

    # Make sure hero content has z-index higher than video
    content = content.replace('<div class="container hero-content">', '<div class="container hero-content" style="position: relative; z-index: 10;">')

    with open(filename, 'w') as f:
        f.write(content)

update_page('shoyu.html', 'https://shoyubros.com/cdn/shop/files/Shoyubros_logo.png', 'assets/shoyu/hero-1.jpg')
update_page('butter.html', 'https://delbocia.com.au/wp-content/uploads/2024/02/logo3.png', 'assets/butter/hero-2.jpg')
update_page('truffles.html', '', 'assets/truffles/hero-1.jpg')
