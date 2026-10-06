with open('p/shoyu.html', 'r') as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    if '641219964_18563161630055656_5378650371683340505_n.jpg' in line:
        count += 1
        # The 1st and 3rd instances correspond to the first duplicate in both the original and repeated blocks
        if count == 1 or count == 3:
            lines[i] = line.replace('641219964_18563161630055656_5378650371683340505_n.jpg', '637704904_18561507334003157_1524865854115677877_n.jpg')

with open('p/shoyu.html', 'w') as f:
    f.writelines(lines)
    
print("Fixed duplicate image in shoyu.html")
