with open('style.css', 'r') as f: css = f.read()

old_wholesale = """.btn-std-wholesale {
    background-color: var(--primary);
    color: var(--charcoal);
    border: 1px solid var(--primary);
}
.btn-std-wholesale:hover {
    background-color: var(--primary-hover);
}"""

new_wholesale = """.btn-std-wholesale {
    background-color: #25D366;
    color: white;
    border: 1px solid #25D366;
}
.btn-std-wholesale:hover {
    background-color: #20BA5A;
    color: white;
}"""

css = css.replace(old_wholesale, new_wholesale)

with open('style.css', 'w') as f: f.write(css)
print("Updated WhatsApp button color")
