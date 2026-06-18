# Week 1 - file organiser
# point it at a messy folder and it sorts the files into Images / PDFs / Documents etc.
# also writes a little log.txt so you can see what got moved where

import os
import shutil

folder = input("Enter the folder path: ")

# open in append mode so we don't wipe an old log if we run it again
log = open(os.path.join(folder, "log.txt"), "a")

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    # skip folders, only want actual files
    if not os.path.isfile(path):
        continue
    # don't move the log or my own script by accident
    if filename == "log.txt" or filename.endswith(".py"):
        continue

    name = filename.lower()   # lower so .JPG and .jpg both match
    if name.endswith((".jpg", ".jpeg", ".png", ".gif")):
        category = "Images"
    elif name.endswith(".pdf"):
        category = "PDFs"
    elif name.endswith((".doc", ".docx", ".txt")):
        category = "Documents"
    elif name.endswith((".mp4", ".mov", ".mkv")):
        category = "Videos"
    elif name.endswith((".mp3", ".wav")):
        category = "Music"
    else:
        category = "Others"   # anything I didn't think of goes here

    new_folder = os.path.join(folder, category)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)   # make the category folder if it's the first one

    shutil.move(path, os.path.join(new_folder, filename))
    log.write(filename + " -> " + category + "\n")
    print(filename, "->", category)

log.close()
print("Done!")
