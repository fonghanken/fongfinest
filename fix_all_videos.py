import re

for page, img in [('p/butter.html', 'hero-2.jpg'), ('p/shoyu.html', 'hero-shoyu.jpg')]:
    with open(page, 'r') as f: html = f.read()
    html = re.sub(
        r'<section class="hero hero-video-container fade-in-up" style="position: relative; overflow: hidden; background-color: #333; background-image: none;">\s*<video[^>]*>.*?<\/video>',
        f'<section class="hero hero-video-container fade-in-up" style="position: relative; overflow: hidden; background-color: #333; background-image: url(\'../assets/{page.split("/")[1].replace(".html","")}/{img}\'); background-size: cover; background-position: center;">',
        html,
        flags=re.DOTALL
    )
    with open(page, 'w') as f: f.write(html)
