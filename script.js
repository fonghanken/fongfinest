document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle (simple implementation)
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const ctaNav = document.querySelector('.cta-nav');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', () => {
            const isDisplayed = window.getComputedStyle(navLinks).display !== 'none';
            if (isDisplayed && window.innerWidth <= 768) {
                navLinks.style.display = 'none';
                if(ctaNav) ctaNav.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '65px';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.backgroundColor = 'rgba(249, 248, 244, 0.98)';
                navLinks.style.padding = '20px';
                navLinks.style.boxShadow = '0 10px 15px rgba(0,0,0,0.05)';
                if(ctaNav) {
                    ctaNav.style.display = 'inline-block';
                    ctaNav.style.margin = '20px auto 0';
                }
            }
        });
    }

    // Scroll Animation Observer
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-in-up');
    fadeElements.forEach(el => observer.observe(el));
    
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
        } else {
            navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.05)';
        }
    });
});
