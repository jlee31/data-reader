import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# read image
image_path = f'images/10-27/{13}.png'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    print(t)

# print(text_)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()