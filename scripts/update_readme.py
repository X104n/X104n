#!/usr/bin/env python3
import os
import random
import json
import datetime
import re

def get_day():
    """Return the current day of the week."""
    return datetime.datetime.now().strftime("%A").lower()

def random_theme(day):
    """Return a random theme based on the day of the week from the JSON file."""
    themes = get_themes_from_day(day)
    return random.choice(themes)

def get_themes_from_day(day):
    with open('scripts/themes.json', 'r') as file:
        all_days = json.load(file)

    this_day = []

    for day_obj in all_days["days"]:
        if day in day_obj:
            this_day.extend(day_obj[day])
    
    print(this_day)
    return this_day


def picture_from_theme(theme):
    """Return a random image from the theme's image folder."""
    # Extract the image folder path from the theme
    theme_name = list(theme.keys())[0]
    image_folder = theme[theme_name]['image-folder']
    
    # Remove leading slash if present
    if image_folder.startswith('/'):
        image_folder = image_folder[1:]
    
    # Get all images from the theme's image directory
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.JPG', '.JPEG', '.PNG', '.GIF']
    images = []
    
    if os.path.exists(image_folder):
        for f in os.listdir(image_folder):
            if any(f.lower().endswith(ext.lower()) for ext in image_extensions):
                images.append(os.path.join(image_folder, f))
    
    if not images:
        print(f"No images found in the {image_folder} directory!")
        return None
    
    # Return a random image from the theme's folder
    return random.choice(images)

def insert_picture(picture, theme):
    readme_path = 'README.md'

    with open(readme_path, 'r') as file:
        content = file.read()
    
    # Update image
    pattern = r'!\[regex\]\([^)]+\)'
    picture_path = picture.replace('\\', '/')
    replacement = f'![regex]({picture_path})'
    updated_content = re.sub(pattern, replacement, content)

    # Update theme text
    theme_name = list(theme.keys())[0]
    theme_pattern = r'Todays theme:.*'
    print(f"Updating theme to: {theme_name}")
    replacement = f'Todays theme: {theme_name}'
    updated_content = re.sub(theme_pattern, replacement, updated_content)
    
    with open(readme_path, 'w') as file:
        file.write(updated_content)
    

if __name__ == "__main__":
    
    day = get_day()

    theme = random_theme(day)

    picture = picture_from_theme(theme)

    if picture:
        insert_picture(picture, theme)
    else:
        print("No picture found to insert.")