with open('index.html', 'r') as f:
    html = f.read()

# 1. No Middleman
no_mid = '<h4>No Middleman</h4>'
no_mid_new = '<h4 style="display: flex; align-items: center; gap: 8px;"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--gold);"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg> No Middleman</h4>'
html = html.replace(no_mid, no_mid_new)

# 2. Pristine Cold-Chain
cold_chain = '<h4>Pristine Cold-Chain</h4>'
# snowflake icon
cold_chain_new = '<h4 style="display: flex; align-items: center; gap: 8px;"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--gold);"><line x1="2" y1="12" x2="22" y2="12"></line><line x1="12" y1="2" x2="12" y2="22"></line><path d="M20 16l-4-4 4-4"></path><path d="M4 8l4 4-4 4"></path><path d="M16 4l-4 4-4-4"></path><path d="M8 20l4-4 4 4"></path></svg> Pristine Cold-Chain</h4>'
html = html.replace(cold_chain, cold_chain_new)

# 3. Exclusivity
exclusive = '<h4>Exclusivity</h4>'
# award icon
exclusive_new = '<h4 style="display: flex; align-items: center; gap: 8px;"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--gold);"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg> Exclusivity</h4>'
html = html.replace(exclusive, exclusive_new)

with open('index.html', 'w') as f:
    f.write(html)
    
print("Updated icons")
