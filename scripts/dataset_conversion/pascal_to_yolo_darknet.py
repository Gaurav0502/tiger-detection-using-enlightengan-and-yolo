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
TRAIN_ANNOT_DIR = "../data/atrw_anno_detection_train(1)/Annotations"
TAGS = ["filename", "size", "width", "height", "depth", "object", "bndbox", "xmin", "xmax", "ymin", "ymax"]

# Convert the annotations from XML to TXT format.
class PASCAL2YOLO:
    
   # Initialize the variables for the class
   def __init__(self, obj_map : dict):
        self.obj_map = obj_map

   # Extraction of the bounding box dimensions by parsing XML.
   def __get_bounding_box_dims(self, id: str):
        # Annotations for one image.
        annot = {"objects": []}
        
        # Parsing the XML annotations file. 
        xml_path = os.path.join(TRAIN_ANNOT_DIR, id+".xml")
        file = ET.parse(xml_path)
        
        # Traversal through the XML Tree.
        root=file.getroot()
        
        for i in root:
            # Filter irrelevant information.
            if i.tag in TAGS:

               if i.tag == "size":

                  img_size = []
                  for img_dim in i:
                    img_size.append(int(img_dim.text))
                  annot[i.tag] = tuple(img_size)

               elif i.tag == "object":
                  tgr = {"name": i[0].text}
                  for bnd_dim in i[-1]:
                    tgr[bnd_dim.tag] = int(bnd_dim.text)
                  annot["objects"].append(tgr)

               else:
                  annot[i.tag] = i.text

        return annot

   # Convert the content to yolo format.
   def __convert_to_txt_format(self, id : str):
      
      # Get bounding box from XML Annotations.
      annot = self.__get_bounding_box_dims(id)
      
      # Get the dimensions of the image for normalization.
      img_h, img_w, img_c = annot["size"]
      new_annotations = []

      for tgr in annot["objects"]:

         # Allot the object IDs
         obj_id = self.obj_map[tgr["name"]]

         # Compute the required descriptors
         xmin = tgr["xmin"]
         xmax = tgr["xmax"]
         ymin = tgr["ymin"]
         ymax = tgr["ymax"]
         center_x = (xmin + xmax)/(2*img_w)
         center_y = (ymin + ymax)/(2*img_h)
         center_w = (xmax - xmin)/img_w
         center_h = (ymax - ymin)/img_h

         # Template to generate content in required format.
         label = "{} {:.3f} {:.3f} {:.3f} {:.3f}".format(obj_id, center_x, center_y, 
                                                         center_w, center_h)

         new_annotations.append(label)
         
      return new_annotations
   
   # Write the annotations of an image to text file.
   def __write_annotations_to_txt(self, id : str):

      # Get the annotations in YOLO darknet format.
      new_annotations = self.__convert_to_txt_format(id)
      txt_path = os.path.join("../data/labels/", id + ".txt")

      fp = open(txt_path, "w")
      fp.write("\n".join(new_annotations))
      fp.close()
   
   # Convert all the annotations to YOLO darknet format.
   def convert_all_annotations(self):

      all_annotations = os.listdir(TRAIN_ANNOT_DIR)
      all_ids = list(map(lambda p: p.replace(".xml", ""), all_annotations))

      for id in all_ids:
         self.__write_annotations_to_txt(id)