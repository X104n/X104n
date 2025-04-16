#!/bin/bash
git config --global user.name 'github-actions[bot]'
git config --global user.email 'github-actions[bot]@users.noreply.github.com'
git add README.md
git diff --quiet && git diff --staged --quiet || git commit -m "Update random profile image"
git push