#!/usr/bin/env python3
import os
import random
import re

def update_readme_with_random_image():
    # Get all images from the images directory
    images = [f for f in os.listdir('images') if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not images:
        print("No images found in the images directory!")
        return
    
    # Pick a random image
    random_image = random.choice(images)
    
    # Read the current README
    with open('README.md', 'r') as file:
        content = file.read()
    
    # Replace the image or add if not exists
    image_pattern = r'!\[Random Image\]\(images/.*?\)'
    image_replacement = f'![Random Image](images/{random_image})'
    
    if re.search(image_pattern, content):
        new_content = re.sub(image_pattern, image_replacement, content)
    else:
        # Add the image at the top if not found
        new_content = f'{image_replacement}\n\n{content}'
    
    # Write updated content back to README
    with open('README.md', 'w') as file:
        file.write(new_content)
    
    print(f"Updated README with random image: {random_image}")

if __name__ == "__main__":
    update_readme_with_random_image()