with open('index.html', 'r') as f: html = f.read()
html = html.replace('Ferrier Winter Truffle', 'Ferrier Black Winter Truffle')
with open('index.html', 'w') as f: f.write(html)

with open('p/truffles.html', 'r') as f: html = f.read()
html = html.replace('Victorian Black Winter Truffle', 'Ferrier Black Winter Truffle')
with open('p/truffles.html', 'w') as f: f.write(html)
