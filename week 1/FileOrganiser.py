import os
import shutil
folder = input("Enter the folder path: ")
log = open(os.path.join(folder, "log.txt"), "a")

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    if not os.path.isfile(path):
        continue
    if filename == "log.txt" or filename.endswith(".py"):
        continue

    name = filename.lower()
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
        category = "Others"

    new_folder = os.path.join(folder, category)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    shutil.move(path, os.path.join(new_folder, filename))
    log.write(filename + " -> " + category + "\n")
    print(filename, "->", category)

log.close()
print("Done!")