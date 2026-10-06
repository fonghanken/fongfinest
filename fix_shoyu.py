with open('p/shoyu.html', 'r') as f: html = f.read()

preload_tags = """    <!-- Preload Hero Assets for Instant Paint -->
    <link rel="preload" as="image" href="../assets/shoyu/hero-1.jpg">
"""
html = html.replace('<meta name="description"', preload_tags + '    <meta name="description"')

# Let's also ensure the video has fetchpriority="high" and preload="auto"
html = html.replace('<video class="hero-video" autoplay loop muted playsinline', '<video class="hero-video" autoplay loop muted playsinline preload="auto" fetchpriority="high"')

with open('p/shoyu.html', 'w') as f: f.write(html)
