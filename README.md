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

## Model Inference
### Requirements
```sh
pip install ultralytics
```
### Sample Code
```python
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Loading the best checkpoint
model = YOLO("weights/best_enlightengan_and_yolov8.pt") # or "weights/best_yolov8.pt" for plain YOLOv8 inference

# For training and validation
model.train(data=path_to_yaml_file, epochs=number_of_epochs)
model.val()

# For testing the model on a test folder
model.val(data=path_to_yaml_file, split="test")

# For testing the model on an image
result = model.predict(source=path_to_image)
annotated = result[0].plot(line_width=linewidth)
plt.imshow(annotated)

```

## Results
- A sample prediction is provided for both cases: YOLOv8 and EnlightenGAN + YOLOv8.

YOLOv8 (Low Illumination)             |  EnlightenGAN + YOLOv8 (Enhanced Illumination)
:-------------------------:|:-------------------------:
![](https://github.com/Gaurav0502/tiger-detection-using-enlightengan-and-yolo/blob/main/data/results/low_illumination.png)  |  ![](https://github.com/Gaurav0502/tiger-detection-using-enlightengan-and-yolo/blob/main/data/results/illuminated.png)

- The results of the training and validation are available in wandb <a href="https://wandb.ai/gauravpendharkar/YOLOv8/">here</a>.

## Conference Paper Citation
```
@article{pendharkar2023efficient,
  title={An Efficient Illumination Invariant Tiger Detection Framework for Wildlife Surveillance},
  author={Pendharkar, Gaurav and Micheal, A Ancy and Misquitta, Jason and Kaippada, Ranjeesh},
  journal={arXiv preprint arXiv:2311.17552},
  year={2023}
}
```

## Referenced GitHub Repositories
- <a href="https://github.com/arsenyinfo/EnlightenGAN-inference">EnlightenGAN Inference</a>
- <a href="https://github.com/VITA-Group/EnlightenGAN">EnligthenGAN (Main Implementation)</a>
- <a href="https://github.com/cvwc2019/ATRWEvalScript">GroundTruth & Eval Scripts for ATRW Dataset</a>
