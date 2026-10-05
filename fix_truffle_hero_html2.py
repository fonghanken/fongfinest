import re
with open('p/truffles.html', 'r') as f: html = f.read()
# Replace the video tag with nothing, and add the background image to the section
html = re.sub(
    r'<section class="hero hero-video-container fade-in-up" style="position: relative; overflow: hidden; background-color: #333; background-image: none;">\s*<video[^>]*>.*?<\/video>',
    '<section class="hero hero-video-container fade-in-up" style="position: relative; overflow: hidden; background-color: #333; background-image: url(\'../assets/truffles/hero.jpg\'); background-size: cover; background-position: center;">',
    html,
    flags=re.DOTALL
)
with open('p/truffles.html', 'w') as f: f.write(html)
