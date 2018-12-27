import cv2
from matplotlib import pyplot as plt
import numpy as np
#import imutils
import os


def colorful(img):

    filter=img*0.6
    filter[:,:,2]=filter[:,:,2]*2.55
    filter[:,:,1]=filter[:,:,1]*2.05
    filter[:,:,0]=filter[:,:,0]*0.8
    filter=np.clip(filter,0,255)
    filter=np.uint8(filter/2)
    return filter

def blur_img(image, coefx,coefy):
	return cv2.blur(image, (coefx,coefy))

path_label="labels"
path_image="images"
path_label_new="labels_new"
path_image_new="images_new"


f3=open("train.txt", "w")
f4=open("label.txt", "w")

for (direpath,dirnames,filenames) in os.walk(path_image):
    for f in filenames:
        files=direpath+'/'+f
        if os.path.isfile(files):
            base=os.path.basename(files)
            name=os.path.splitext(base)[0]
            print("image:",files)
            image = cv2.imread(files)
            scale_x=np.random.randint(5,25)
            scale_y=np.random.randint(5,15)
            image=blur_img(image, scale_x,scale_y)
            image=colorful(image)


            path_n_i=path_image_new+"/blur_"+name+".jpg"
            path_n_l=path_label_new+"/blur_"+name+".txt"
            f3.write("%s\n" %(path_n_i))
            f4.write("%s\n" %(path_n_l))
            cv2.imwrite(path_n_i, image)
            with open(path_label+"/"+name+".txt") as f:
                with open(path_n_l, "w") as f1:
                    for line in f:
                        f1.write(line)
