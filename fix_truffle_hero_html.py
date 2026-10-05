with open('p/truffles.html', 'r') as f: html = f.read()
html = html.replace('poster="../assets/truffles/hero-1.jpg"', 'poster="../assets/truffles/hero.jpg"')
with open('p/truffles.html', 'w') as f: f.write(html)
