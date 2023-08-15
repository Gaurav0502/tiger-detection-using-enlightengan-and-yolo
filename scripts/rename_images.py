import os

TARGET_DIR = "final_images/"

all_files = os.listdir(TARGET_DIR)

c = 0

for img_file in all_files:
    img_path = os.path.join(TARGET_DIR, img_file)
    new_path = os.path.join(TARGET_DIR, 
                            "W_"+str(c).rjust(4, "0")+"."+img_file.split(".")[-1])
    os.rename(img_path, new_path)
    c += 1
