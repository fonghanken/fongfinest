with open('style.css', 'r') as f: css = f.read()

old_css = """.infinite-carousel img {
    height: 250px;
    width: auto;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}"""

new_css = """.infinite-carousel img {
    height: 250px;
    width: 250px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}"""

css = css.replace(old_css, new_css)
with open('style.css', 'w') as f: f.write(css)
print("Updated CSS to fix carousel speed")
