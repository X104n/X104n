#!/usr/bin/env python3
import os
import random

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
    
    # Create new README with just the image
    image_content = f'## New image every day!\n![Random Image](images/{random_image})'
    
    # Write to README.md
    with open('README.md', 'w') as file:
        file.write(image_content)
    
    print(f"Successfully updated README with only the random image: {random_image}")

if __name__ == "__main__":
    update_readme_with_random_image()
