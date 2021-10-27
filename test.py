import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

dir = 'C:\\Users\\Richie Lee\\Desktop\\College\\1 San Jose State University\\9 2021 fall semester\\CMPE 188\\hw2&hw3\\photos\\train_set'
train_dir = './photos/train_set/'
test_dir = './photos/test_set/'

targets = ['buildings','forest','glacier','mountain','sea','street']
data = []

for target in targets:
    path = os.path.join(train_dir,target)
    label = targets.index(target)
    
    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        train_img = cv2.imread(imgpath)
        try:
            train_img = cv2.resize(train_img,(120,120))
            image = np.array(train_img).flatten()
            data.append([image,label])
            
        except Exception as e:
            pass
print(len(data))
        