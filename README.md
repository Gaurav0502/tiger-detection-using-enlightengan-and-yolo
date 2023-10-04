# Real-Time Tiger Spotting for Wildlife Sanctuaries
## Aim
In this repository, tiger detection is implemented using YOLOv8 from Ultralytics. Moreover, the issue of Low Illumination Images is handled by the using EnlightenGAN for Image Enhancement.

## Datasets 
- The ATRW dataset is used for the project. It is published in <a href="https://arxiv.org/abs/1906.05586">this paper</a> .
- The ATRW dataset comprises train and validation data in PASCAL VOC format and testing data in COCO format. Both of them are converted in YOLO Darknet format as expected by Ultralytics. The dataset is open-source and available in Kaggle <a href="https://www.kaggle.com/datasets/gauravpendharkar/tiger-detection-dataset">here</a>.
- The images in ATRW dataset are enhanced in terms of illumination using EnlightenGAN and the enhanced dataset is made available <a href="https://www.kaggle.com/datasets/gauravpendharkar/enlightengan-results-for-atrw-dataset">here</a>.

## Results
The results of the training and validation are available in wandb <a href="https://wandb.ai/gauravpendharkar/YOLOv8/">here</a>.
