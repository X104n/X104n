#!/usr/bin/env python3
import os
import random
import re

def update_readme_with_random_image():
    # Print working directory and list files for debugging
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in images directory: {os.listdir('images') if os.path.exists('images') else 'images directory not found'}")
    
    # Get all images from the images directory (case insensitive extension matching)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.JPG', '.JPEG', '.PNG', '.GIF']
    images = []
    
    if os.path.exists('images'):
        for f in os.listdir('images'):
            if any(f.lower().endswith(ext.lower()) for ext in image_extensions):
                images.append(f)
    
    if not images:
        print("No images found in the images directory!")
        return
    
    print(f"Found {len(images)} images: {images}")
    
    # Pick a random image
    random_image = random.choice(images)
    print(f"Selected random image: {random_image}")
    
    # Read the current README
    with open('README.md', 'r') as file:
        content = file.read()
    
    # Replace the image or add if not exists
    # Use a more flexible pattern that will match various image references
    image_pattern = r'!\[.*?\]\(images/.*?\)'
    image_replacement = f'![Random Image](images/{random_image})'
    
    if re.search(image_pattern, content):
        new_content = re.sub(image_pattern, image_replacement, content)
        print("Replaced existing image reference in README")
    else:
        # Add the image at the top if not found
        new_content = f'{image_replacement}\n\n{content}'
        print("Added new image reference to README")
    
    # Write updated content back to README
    with open('README.md', 'w') as file:
        file.write(new_content)
    
    print(f"Successfully updated README with random image: {random_image}")

if __name__ == "__main__":
    update_readme_with_random_image()