#!/bin/bash

# Prompt for commit message
read -p "Enter your commit message, then press Enter: " commit_message

# Check if the commit message is empty
if [ -z "$commit_message" ]; then
  echo "Error: Commit message cannot be empty."
  exit 1
fi

# Stage all changes
git add .

# Check if there are any changes to commit
if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

# Commit with the provided message
git commit -m "$commit_message"

# Push changes to the remote repository (modify 'main' to your branch if necessary)
git push origin main
