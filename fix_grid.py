import re

with open('index.html', 'r') as f:
    html = f.read()

# The grid currently in the #provenance section is the value-prop-card one with 'mt-6'.
# Or wait, let's just find the whole <div class="grid mt-6"...> block and replace it.

new_grid = '''
                <div class="grid advantage-grid mt-6">
                    <div class="advantage-item fade-in-up" style="transition-delay: 0.1s;">
                        <span class="advantage-number">01</span>
                        <h4>No Middleman</h4>
                        <p>Direct importers, controlling the supply chain from producer to pass — end to end, with nothing lost between.</p>
                    </div>
                    <div class="advantage-item fade-in-up" style="transition-delay: 0.2s;">
                        <span class="advantage-number">02</span>
                        <h4>Pristine Cold-Chain</h4>
                        <p>Strict cold-chain handling, prioritized from the port of entry directly to your premises, ensuring perfect integrity.</p>
                    </div>
                    <div class="advantage-item fade-in-up" style="transition-delay: 0.3s;">
                        <span class="advantage-number">03</span>
                        <h4>Fully Licensed</h4>
                        <p>Operating under SFA, NParks, and SPF licenses, so every delivery arrives with paperwork you can trust.</p>
                    </div>
                    <div class="advantage-item fade-in-up" style="transition-delay: 0.4s;">
                        <span class="advantage-number">04</span>
                        <h4>Authentic Heritage</h4>
                        <p>Partnering with multigenerational artisans who respect the old ways of food crafting.</p>
                    </div>
                    <div class="advantage-item fade-in-up" style="transition-delay: 0.5s;">
                        <span class="advantage-number">05</span>
                        <h4>Guaranteed Freshness</h4>
                        <p>We skip the middlemen, ensuring absolute freshness and direct relationships with the source.</p>
                    </div>
                    <div class="advantage-item fade-in-up" style="transition-delay: 0.6s;">
                        <span class="advantage-number">06</span>
                        <h4>Restaurant Quality</h4>
                        <p>Supplying high-end ingredients that top chefs in Singapore demand for their kitchens.</p>
                    </div>
                </div>
'''

# 1. Remove <h3 class="section-title text-center fade-in-up" style="margin-top: 60px;">Provisions the way they should be.</h3>
html = re.sub(r'<h3 class="section-title text-center fade-in-up" style="margin-top: 60px;">Provisions the way they should be\.</h3>\s*', '', html)

# 2. Replace the value-prop-card grid with new_grid
grid_pattern = r'<div class="grid mt-6" style="grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 30px;">.*?</div>\s*</div>\s*</div>\s*</section>'
html = re.sub(grid_pattern, new_grid.strip() + '\n            </div>\n        </section>', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
