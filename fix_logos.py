for file in ['p/shoyu.html', 'p/butter.html']:
    with open(file, 'r') as f:
        content = f.read()

    # Apply filter: invert(1) brightness(0) or just brightness(0) or contrast. 
    # Let's use brightness(0) to make it solid black/charcoal if it's transparent white PNG.
    # Actually, var(--charcoal) is #1a1a1a. brightness(0) makes it black #000.
    # Let's add style filter: invert(1) if it's white, but brightness(0) is safer.
    content = content.replace('style="max-height: 80px; margin: 0 auto 20px; display: block;"', 'style="max-height: 80px; margin: 0 auto 20px; display: block; filter: brightness(0); opacity: 0.9;"')
    
    with open(file, 'w') as f:
        f.write(content)
