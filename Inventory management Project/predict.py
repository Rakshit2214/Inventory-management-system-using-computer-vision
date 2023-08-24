import streamlit as st
from PIL import Image
import cv2
from tqdm import tqdm
import os
import pickle,json,itertools,random
import imgaug.augmenters as iaa
import imgaug.imgaug
import numpy as np
import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from dbintegration import *

def load_image(image_file):
	img = Image.open(image_file)
	return img

def augment_add(images, seq):

    augmented_images = []
    for idx,img in tqdm(enumerate(images)):

        image_aug_1 = seq.augment_image(image=img)
        image_aug_2 = seq.augment_image(image=img)
        augmented_images.append(image_aug_1)
        augmented_images.append(image_aug_2)


    augmented_images = np.array(augmented_images, dtype=np.float32)

    return (augmented_images)
    pass

def checkup():
    itname =[]
    itcount=[]
    iname=retname()
    icount=retcount()
    for i in range(5) :
        itname.append(iname[i][0])
        itcount.append(icount[i][0])

    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: white;'>Current Inventory :</h3>", unsafe_allow_html=True)
    fig = go.Figure(data=[go.Table (
        columnwidth = [700,700],
        header=dict(values=['Item','Count'], fill_color='paleturquoise', font=dict(color='black'), font_size = 20),
        cells=dict(values=[itname, itcount,], fill_color='lavender', font=dict(color='black'), font_size = 14, height=30))
        ])
    st.plotly_chart(fig, use_container_width=True)

def countproducts(res,pname):
        clist = []
        for i in range(5):
            clist.append(res.count(pname[i]))
        return clist

def maketable(pname,clist):
    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: white;'>Item Summary :</h3>", unsafe_allow_html=True)
    fig = go.Figure(data=[go.Table (
        columnwidth = [700,700],
        header=dict(values=['Item:','Count:'], fill_color='paleturquoise', font=dict(color='black'), font_size = 20),
        cells=dict(values=[pname, clist], fill_color='lavender', font=dict(color='black'), font_size = 14, height=30))
        ])
    st.plotly_chart(fig, use_container_width=True)
    
def final():
    pname=['MILK',"NUTS","OIL","SODA","TEA"]

    count_f=0
    images = []
    for file in tqdm(os.listdir("C:\\Users\\91982\\Desktop\\fda project\\product_test")) :
        img_path  = os.path.join("C:\\Users\\91982\\Desktop\\fda project\\product_test", file)
        img =cv2.imread(img_path)
        img = cv2.resize(img, (96,96))
        images.append(img)
        count_f+=1

    seq = iaa.Sequential([
        iaa.Fliplr(0.5),
        iaa.Crop(percent=(0,0.1)),
        iaa.LinearContrast((0.75,1.5)),
        iaa.Multiply((0.8,1.2), per_channel=0.2),
        iaa.Affine(
            scale={'x':(0.8,1.2), "y":(0.8,1.2)},
            translate_percent={"x":(-0.2,0.2),"y":(-0.2,0.2)},
            rotate=(-25,25),
            shear=(-8,8)
        )
    ], random_order=True)

    (aug_images) = augment_add(images, seq)
    images = np.concatenate([images, aug_images])  
    images = np.array(images,dtype=np.float32)/255.0  
    newmodel = tf.keras.models.load_model("model.h5")
    result = newmodel.predict(images)
    test_pred = np.argmax(result,axis=1)
    class_name = ["MILK","NUTS","OIL","SODA","TEA"]
    class_name_labels={'MILK': 0, 'NUTS': 1, 'OIL': 2, 'SODA': 3, 'TEA': 4}
    class_labels = {i:class_name for (class_name,i) in class_name_labels.items()}
    res=[]

    for i in range(count_f):
        res.append(class_labels[test_pred[i]])


    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: white;'>Images Recognised :</h3>", unsafe_allow_html=True)
    fig = go.Figure(data=[go.Table (
        columnwidth = [700],
        header=dict(values=['Products: '], fill_color='paleturquoise', font=dict(color='black'), font_size = 20),
        cells=dict(values=[ res], fill_color='lavender', font=dict(color='black'), font_size = 14, height=30))
        ])
    st.plotly_chart(fig, use_container_width=True)

    clist = countproducts(res,pname)
    cost=[78,256,199,256,100]
    cnt=0



    if(st.button("Checkout: ")):
            updatevals2(pname,clist)
            for i in range(len(clist)) :
                cnt+=clist[i]*cost[i]
            st.warning('Items bought successfuly')
            st.write('Checkout Price : ',cnt)
            checkup()
            maketable(pname,clist)


