with open('p/shoyu.html', 'r') as f:
    shoyu = f.read()
shoyu = shoyu.replace('https://shoyubros.com/cdn/shop/files/Shoyubros_logo.png', '../assets/shoyu/logo.png')
with open('p/shoyu.html', 'w') as f:
    f.write(shoyu)

with open('p/butter.html', 'r') as f:
    butter = f.read()
butter = butter.replace('https://delbocia.com.au/wp-content/uploads/2024/02/logo3.png', '../assets/butter/logo.png')
with open('p/butter.html', 'w') as f:
    f.write(butter)
