import os
import glob

directory = r"C:\Users\Alus\Documents"

extensions = set()

# Get all files in the directory and its subdirectories
files = glob.glob(os.path.join(directory, "**"), recursive=True)

# Iterate over the files and collect the unique extensions
for file in files:
    if os.path.isfile(file):
        _, extension = os.path.splitext(file)
        extensions.add(extension.lower())

# Print the unique file extensions found
for extension in extensions:
    print(extension)
