with open('script.js', 'r') as f:
    js = f.read()

target = """                if(navActions) {
                    navLinks.style.paddingBottom = '10px';
                    navLinks.style.boxShadow = 'none';
                    
                    navActions.style.display = 'flex';
                    navActions.style.justifyContent = 'center';
                    navActions.style.padding = '10px 20px 30px 20px';
                    navActions.style.backgroundColor = 'rgba(19, 35, 32, 0.98)';
                    navActions.style.position = 'absolute';
                    navActions.style.top = (65 + navLinks.offsetHeight) + 'px';
                    navActions.style.left = '0';
                    navActions.style.width = '100%';
                    navActions.style.boxShadow = '0 10px 15px rgba(0,0,0,0.5)';
                } else {
                    navLinks.style.boxShadow = '0 10px 15px rgba(0,0,0,0.5)';
                }"""

replacement = """                const shouldShowActions = navActions && !navActions.classList.contains('nav-actions-hidden');
                if(shouldShowActions) {
                    navLinks.style.paddingBottom = '10px';
                    navLinks.style.boxShadow = 'none';
                    
                    navActions.style.display = 'flex';
                    navActions.style.justifyContent = 'center';
                    navActions.style.padding = '10px 20px 30px 20px';
                    navActions.style.backgroundColor = 'rgba(19, 35, 32, 0.98)';
                    navActions.style.position = 'absolute';
                    navActions.style.top = (65 + navLinks.offsetHeight) + 'px';
                    navActions.style.left = '0';
                    navActions.style.width = '100%';
                    navActions.style.boxShadow = '0 10px 15px rgba(0,0,0,0.5)';
                } else {
                    navLinks.style.boxShadow = '0 10px 15px rgba(0,0,0,0.5)';
                    if(navActions) navActions.style.display = 'none';
                }"""

js = js.replace(target, replacement)

# We also need to hide it if they scroll and it crosses the threshold while the menu is open.
# But actually, when the mobile menu is open, the user usually doesn't scroll. If they do, we can update it in updateNavActionsVisibility.
# updateNavActionsVisibility needs to also hide it if window.innerWidth <= 768.

with open('script.js', 'w') as f:
    f.write(js)
print("Updated script.js")
