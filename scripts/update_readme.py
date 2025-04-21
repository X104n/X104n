#!/usr/bin/env python3
import os
import random
import json
import datetime

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
    return "a"

def insert_picture(picture):
    return "b"

if __name__ == "__main__":
    
    day = get_day()

    theme = random_theme(day)

    print(f"Today's theme is: {theme}")

    picture = picture_from_theme(theme)

    insert_picture(picture)