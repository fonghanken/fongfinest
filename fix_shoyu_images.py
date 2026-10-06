import re

with open('p/shoyu.html', 'r') as f:
    html = f.read()

# Replace images
html = html.replace('480594498_659499276421096_127861401355362872_n.jpg', '641219964_18563161630055656_5378650371683340505_n.jpg')
html = html.replace('551983832_1413553913062434_4242947057735572850_n.jpg', '641219964_18563161630055656_5378650371683340505_n.jpg')
html = html.replace('BDP06300resized_5af231dc-05b0-4167-9db8-c96b5a664326_720x.jpg', '328259021_6011536548884762_2778400187351916573_n.jpg')

# Remove the og-image section
img_block_regex = r'<div style="margin: 40px 0;">\s*<img src="\.\./assets/shoyu/og-image\.jpg"[^>]*>\s*</div>'
html = re.sub(img_block_regex, '', html)

# Remove the poster attribute from the video
html = html.replace('poster="../assets/shoyu/hero-1.jpg"', '')

with open('p/shoyu.html', 'w') as f:
    f.write(html)
    
print("Updated shoyu.html")
