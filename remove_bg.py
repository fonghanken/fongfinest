from PIL import Image

def remove_background(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    
    datas = img.getdata()
    
    # Assume the top-left pixel is the background color
    bg_color = datas[0]
    
    # We'll tolerate a small variance (for jpeg artifacts)
    tolerance = 30
    
    newData = []
    for item in datas:
        # Check if the pixel color is close to the background color
        if (abs(item[0] - bg_color[0]) < tolerance and
            abs(item[1] - bg_color[1]) < tolerance and
            abs(item[2] - bg_color[2]) < tolerance):
            # Replace with transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    
    # Crop to bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(output_path, "PNG")

try:
    remove_background('/Users/hanken/Desktop/fongenterprise/6_Media_Library/delbocia_logo.jpeg', 'assets/butter/logo.png')
    print("Background removed and saved as assets/butter/logo.png")
except Exception as e:
    print("Error:", e)

