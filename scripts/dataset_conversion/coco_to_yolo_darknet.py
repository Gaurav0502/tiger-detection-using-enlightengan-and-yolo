# Modules used for handling data
import numpy as np
# Modules used for computer vision
import cv2

# Modules used for handling files
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
import json
import shutil

# Modules used for randomization
import random as r
import pprint

# Constants
TEST_DIR = "../data/atrw_detection_test/test/"

# Convert the annotations from JSON to TXT format.
class COCO2YOLO:

    # Initialize the variables for the class
    def __init__(self, obj_map : dict, annotations : list):
        self.obj_map = obj_map
        self.annotations = annotations
    
    def __get_dims(self, id : str):
        img_id = int(id)
        annot = {"objects": []}
        annot["filename"] = img_id

        for i in annotations["annotations"]:
            if i["image_id"] == img_id:
               tgr = {"name": "Tiger"}
               tgr["x"], tgr["y"], tgr["w"], tgr["h"] = i["bbox"]
               annot["objects"].append(tgr)
        
        return annot

    def __convert_txt_format(self, id : str):
      annot = self.__get_dims(id)
      #pprint.pprint(annot)
      img_h, img_w, img_c = (1920, 1080, 3)
      new_annotations = []

      for tgr in annot["objects"]:

         obj_id = self.obj_map[tgr["name"]]

         x = tgr["x"]
         y = tgr["y"]
         w = tgr["w"]
         h = tgr["h"]

         center_x = (x + (x + w))/(2*img_w)
         center_y = (y + (y + h))/(2*img_h)
         center_w = w/img_w
         center_h = h/img_h

         label = "{} {:.3f} {:.3f} {:.3f} {:.3f}".format(obj_id, center_x, center_y, 
                                                         center_w, center_h)

         new_annotations.append(label)
         
      return new_annotations

    def __write_annotations_to_txt(self, id : str):
      #print("Entered")
      new_annotations = self.__convert_txt_format(id)
      txt_path = os.path.join("../data/labels/test", id + ".txt")

      fp = open(txt_path, "w")
      fp.write("\n".join(new_annotations))
      fp.close()
    
    
    def convert_all_annotations(self):

      all_annotations = os.listdir(TEST_DIR)
      all_ids = list(map(lambda p: p.replace(".jpg", ""), all_annotations))

      for id in all_ids:
         self.__write_annotations_to_txt(id)