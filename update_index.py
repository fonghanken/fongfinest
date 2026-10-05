import re

with open('index.html', 'r') as f:
    content = f.read()

# Add marquee and main overlap
main_pattern = r'(<main>)'
marquee_html = '''<main>
        <div class="main-overlap">
            <div class="marquee-container">
                <div class="marquee-content">
                    EXCLUSIVE DISTRIBUTORS &nbsp;⭑&nbsp; DIRECT IMPORT &nbsp;⭑&nbsp; RESTAURANT QUALITY &nbsp;⭑&nbsp; 100% ARTISANAL &nbsp;⭑&nbsp; FAMILY HERITAGE &nbsp;⭑&nbsp; EXCLUSIVE DISTRIBUTORS &nbsp;⭑&nbsp; DIRECT IMPORT &nbsp;⭑&nbsp; RESTAURANT QUALITY &nbsp;⭑&nbsp; 100% ARTISANAL &nbsp;⭑&nbsp; FAMILY HERITAGE &nbsp;⭑&nbsp;
                </div>
            </div>'''
content = re.sub(main_pattern, marquee_html, content)

# Add closing div for main-overlap before </main>
content = content.replace('</main>', '</div>\n    </main>')

# Add Value Proposition Section right before Portfolio Section
portfolio_pattern = r'(<!-- Portfolio Section -->)'
value_prop_html = '''<!-- Value Proposition Section -->
        <section class="section">
            <div class="container">
                <h2 class="section-title text-center fade-in-up">Provisions the way they should be.</h2>
                <div class="grid mt-6" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
                    <div class="value-prop-card fade-in-up">
                        <div class="value-prop-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                        </div>
                        <h3 class="card-title mt-2 text-center" style="font-size: 1.5rem;">Authentic Heritage</h3>
                        <p class="card-desc text-center mt-2">Partnering with multigenerational artisans who respect the old ways of food crafting.</p>
                    </div>
                    <div class="value-prop-card fade-in-up" style="transition-delay: 0.1s;">
                        <div class="value-prop-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>
                        </div>
                        <h3 class="card-title mt-2 text-center" style="font-size: 1.5rem;">Direct Import</h3>
                        <p class="card-desc text-center mt-2">We skip the middlemen, ensuring absolute freshness and direct relationships with the source.</p>
                    </div>
                    <div class="value-prop-card fade-in-up" style="transition-delay: 0.2s;">
                        <div class="value-prop-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
                        </div>
                        <h3 class="card-title mt-2 text-center" style="font-size: 1.5rem;">Restaurant Quality</h3>
                        <p class="card-desc text-center mt-2">Supplying high-end ingredients that top chefs in Singapore demand for their kitchens.</p>
                    </div>
                </div>
            </div>
        </section>
        
        \\1'''
content = re.sub(portfolio_pattern, value_prop_html, content)

with open('index.html', 'w') as f:
    f.write(content)
