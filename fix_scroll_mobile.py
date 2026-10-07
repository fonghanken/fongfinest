with open('script.js', 'r') as f:
    js = f.read()

target = """        if (hideAtTop || hideAtBottom) {
            navActionsBlock.classList.add('nav-actions-hidden');
        } else {
            navActionsBlock.classList.remove('nav-actions-hidden');
        }"""

replacement = """        if (hideAtTop || hideAtBottom) {
            navActionsBlock.classList.add('nav-actions-hidden');
            if (window.innerWidth <= 768) {
                navActionsBlock.style.display = 'none';
                const navLinks = document.querySelector('.nav-links');
                if (navLinks && navLinks.style.display === 'flex') {
                    navLinks.style.boxShadow = '0 10px 15px rgba(0,0,0,0.5)';
                    navLinks.style.paddingBottom = '20px';
                }
            }
        } else {
            navActionsBlock.classList.remove('nav-actions-hidden');
            if (window.innerWidth <= 768) {
                const navLinks = document.querySelector('.nav-links');
                if (navLinks && navLinks.style.display === 'flex') {
                    navLinks.style.paddingBottom = '10px';
                    navLinks.style.boxShadow = 'none';
                    navActionsBlock.style.display = 'flex';
                    navActionsBlock.style.justifyContent = 'center';
                    navActionsBlock.style.padding = '10px 20px 30px 20px';
                    navActionsBlock.style.backgroundColor = 'rgba(19, 35, 32, 0.98)';
                    navActionsBlock.style.position = 'absolute';
                    navActionsBlock.style.top = (65 + navLinks.offsetHeight) + 'px';
                    navActionsBlock.style.left = '0';
                    navActionsBlock.style.width = '100%';
                    navActionsBlock.style.boxShadow = '0 10px 15px rgba(0,0,0,0.5)';
                } else {
                    navActionsBlock.style.display = 'none';
                }
            } else {
                navActionsBlock.style.display = '';
            }
        }"""

js = js.replace(target, replacement)
with open('script.js', 'w') as f:
    f.write(js)
