#!/usr/bin/env python3
import os
import random

def update_readme_with_random_image():
    
    images = get_images()
    print(f"Found {len(images)} images: {images}")

    random_image = get_random_image(images)
    image_content = f'''## New image every day!\n![Random Image](images/{random_image})'''
    
    with open('README.md', 'w') as file:
        file.write(image_content)
    
    print(f"Successfully updated README with: {random_image}")

def get_images():
    
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
    
    return images

def get_random_image(images):
        # Pick a random image
    with open('README.md', 'r') as file:
        readme = file.read()
        currentImage = readme[47:-1:]
    
    while True:
        random_image = random.choice(images)
        print(f"Selected random image: {random_image}")
        if currentImage == random_image:
            continue
        else:
            break

    return random_image

if __name__ == "__main__":
    update_readme_with_random_image()
