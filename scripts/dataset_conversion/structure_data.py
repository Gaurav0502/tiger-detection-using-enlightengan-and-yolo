# Modules used for handling files
import os
import json
import shutil

# Constants
TRAIN_DIR = "../data/atrw_detection_train/trainval"
TEST_DIR = "../data/atrw_detection_test/test/"
PATH = "../data/atrw_anno_detection_train(1)/ImageSets/Main"
TRAINVAL_LABELS = "../data/labels/trainval/"

# Get the images for training and validation sets.
train_images_fp = open(os.path.join(path, "train.txt"), "r")
train_images_id = train_images_fp.read().split("\n")

val_images_fp = open(os.path.join(path, "val.txt"), "r")
val_images_id = val_images_fp.read().split("\n")


src_root = "../data/labels/trainval/"
dst_root = "../final_data/labels"

# Copy train labels to appropriate locations.
for i in train_images_id:
    if i != "":
        shutil.copy(os.path.join(src_root, i + ".txt"), os.path.join(dst_root, "train", i + ".txt"))

# Copy validation labels to appropriate locations.
for i in val_images_id:
    if i != "":
        shutil.copy(os.path.join(src_root, i + ".txt"), os.path.join(dst_root, "val", i + ".txt"))

# Copy the test labels to appropriate locations.
src_root = "../data/labels/test/"
dst_root = "../final_data/labels/"

for i in os.listdir(src_root):
    if i != "":
        shutil.copy(os.path.join(src_root, i), os.path.join(dst_root, "test", i))