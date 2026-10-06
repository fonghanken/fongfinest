import re

with open('style.css', 'r') as f: css = f.read()

# Remove the media query rules
css = re.sub(r'\s*\.floating-btn \{[^}]+\}', '', css)
css = re.sub(r'\s*\.floating-btn svg \{[^}]+\}', '', css)
css = re.sub(r'\s*\.floating-btn:hover \{[^}]+\}', '', css)

with open('style.css', 'w') as f: f.write(css)
print("Cleaned CSS.")
