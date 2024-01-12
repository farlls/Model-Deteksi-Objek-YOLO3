# Import libraries
import cv2
import numpy as np
from PIL import Image
from cvlib.object_detection import detect_common_objects, draw_bbox
import matplotlib.pyplot as plt

# Read images
img = Image.open('./data_img/coffee.jpg')
img = np.array(img)

# Detect and drawbox around objects
bbox, label, conf = detect_common_objects(img, model='yolov3')
output_image = draw_bbox(img, bbox, label, conf)

# Plot the image with predictions
plt.imshow(output_image)
plt.show()