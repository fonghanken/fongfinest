from PIL import Image, ImageDraw

def apply_circular_mask(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Ensure it's square
    min_dim = min(width, height)
    left = (width - min_dim)/2
    top = (height - min_dim)/2
    right = (width + min_dim)/2
    bottom = (height + min_dim)/2
    
    img = img.crop((left, top, right, bottom))
    
    # Create a circular mask
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, min_dim, min_dim), fill=255)
    
    # Apply mask
    result = Image.new('RGBA', img.size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask=mask)
    
    # Also trim any extra transparent edges if it wasn't filling the whole circle
    bbox = result.getbbox()
    if bbox:
        result = result.crop(bbox)
        
    result.save(output_path, "PNG")

apply_circular_mask('/Users/hanken/Desktop/fongenterprise/6_Media_Library/delbocia_logo.webp', 'assets/butter/logo.webp')
print("Circular crop applied.")
