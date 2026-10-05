with open('style.css', 'r') as f:
    css = f.read()

# Replace the last appended block with a simpler one
css = css.replace('''
.portfolio-section {
    background-color: var(--charcoal);
    color: var(--foreground);
    border-radius: 40px 40px 0 0;
    margin-top: -40px;
    position: relative;
    z-index: 25;
}''', '''
.portfolio-section {
    background-color: var(--charcoal);
    color: var(--foreground);
}''')

with open('style.css', 'w') as f:
    f.write(css)
