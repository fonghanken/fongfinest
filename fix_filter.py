import re

for file in ['p/shoyu.html', 'p/butter.html']:
    with open(file, 'r') as f:
        content = f.read()
    
    # Remove the invert filter so gold elements and original colors show through
    content = content.replace('filter: brightness(0) invert(1); opacity: 0.9;', 'opacity: 0.9;')
    
    with open(file, 'w') as f:
        f.write(content)

