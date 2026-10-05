import os
import shutil

src_dir = '/Users/hanken/Desktop/fongenterprise/5_Products_Operations/Fong_Finest_Project/assets/photos/truffles'
gallery_dir = 'assets/truffles/gallery'
hero_dest = 'assets/truffles/hero.jpg'

carousel_imgs = set(os.listdir(gallery_dir))
all_imgs = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])

new_hero = None
for img in all_imgs:
    if img not in carousel_imgs:
        new_hero = img
        break

if new_hero:
    print(f"Setting new hero image: {new_hero}")
    shutil.copy(os.path.join(src_dir, new_hero), hero_dest)
else:
    print("No unused images found!")
