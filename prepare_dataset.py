import os
import shutil

# Correct source directory
SOURCE_DIR = r"C:\Users\mlv67131\Documents\Summer_Research\plantdisease\PlantVillage"
TARGET_DIR = "dataset"

# Use folder names that exist
healthy_folders = ["Tomato_healthy"]
diseased_folders = [
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Bacterial_spot",
    "Tomato_Leaf_Mold"
]

# Create target folders
os.makedirs(os.path.join(TARGET_DIR, "healthy"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "diseased"), exist_ok=True)

# Copy healthy images
for folder in healthy_folders:
    folder_path = os.path.join(SOURCE_DIR, folder)
    if not os.path.exists(folder_path):
        print(f"⚠️ Skipping missing folder: {folder}")
        continue
    for file in os.listdir(folder_path):
        src = os.path.join(folder_path, file)
        dst = os.path.join(TARGET_DIR, "healthy", file)
        shutil.copyfile(src, dst)

# Copy diseased images
for folder in diseased_folders:
    folder_path = os.path.join(SOURCE_DIR, folder)
    if not os.path.exists(folder_path):
        print(f"⚠️ Skipping missing folder: {folder}")
        continue
    for file in os.listdir(folder_path):
        src = os.path.join(folder_path, file)
        dst = os.path.join(TARGET_DIR, "diseased", file)
        shutil.copyfile(src, dst)

print("✅ Dataset prepared in 'dataset/' folder.")
