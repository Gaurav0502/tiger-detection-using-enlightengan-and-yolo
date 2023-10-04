# Real-Time Tiger Spotting for Wildlife Sanctuaries
## Aim
In this repository, tiger detection is implemented using YOLOv8 from Ultralytics. Moreover, the issue of Low Illumination Images is handled by the using EnlightenGAN for Image Enhancement.

## Datasets 
- The ATRW dataset is used for the project. It is published in <a href="https://arxiv.org/abs/1906.05586">this paper</a> .
- The ATRW dataset comprises train and validation data in PASCAL VOC format and testing data in COCO format. Both of them are converted in YOLO Darknet format as expected by Ultralytics. The dataset is open-source and available in Kaggle <a href="https://www.kaggle.com/datasets/gauravpendharkar/tiger-detection-dataset">here</a>.
- The images in ATRW dataset are enhanced in terms of illumination using EnlightenGAN and the enhanced dataset is made available <a href="https://www.kaggle.com/datasets/gauravpendharkar/enlightengan-results-for-atrw-dataset">here</a>.

## Kaggle Notebooks
The tasks of Tiger Detection and Image Enhancement were carried out in Kaggle using GPU P100. The codes can be found in the respective notebooks:

- <a href="https://www.kaggle.com/code/gauravpendharkar/tiger-detection-using-yolo-and-enlightengan"> Tiger Detection using YOLOv8 (for both cases) </a>
- <a href="https://www.kaggle.com/code/gauravpendharkar/enlightengan-with-cudaexecutionprovider"> Image Enhancement using EnlightenGAN </a> 

## Results
- A sample prediction is provided for both cases: YOLOv8 and EnlightenGAN + YOLOv8.

YOLOv8 (Low Illumination)             |  EnlightenGAN + YOLOv8 (Enhanced Illumination)
:-------------------------:|:-------------------------:
![](https://github.com/Gaurav0502/tiger-detection-using-enlightengan-and-yolo/blob/main/data/results/low_illumination.png)  |  ![](https://github.com/Gaurav0502/tiger-detection-using-enlightengan-and-yolo/blob/main/data/results/illuminated.png)

- The results of the training and validation are available in wandb <a href="https://wandb.ai/gauravpendharkar/YOLOv8/">here</a>.

## Referenced GitHub Repositories
- <a href="https://github.com/arsenyinfo/EnlightenGAN-inference">EnligthenGAN Inference</a>
- <a href="https://github.com/VITA-Group/EnlightenGAN">EnligthenGAN (Main Implementation)</a>
- <a href="https://github.com/cvwc2019/ATRWEvalScript">GroundTruth & Eval Scripts for ATRW Dataset</a>
