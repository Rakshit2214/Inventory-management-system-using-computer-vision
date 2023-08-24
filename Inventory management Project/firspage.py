from logging import PlaceHolder
import streamlit as st
import pandas as pd
import webbrowser
import homenew
import update
import buy
import predict

# import customtest
# import algosummary
# import testsample
# import more

st.markdown("<h1 style='text-align: center; color: lightblue;'>FDA Project Prototype</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: skyblue;'>Inventory Management using Image Recognition</h4>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: yellow ;'>⚡Model⚡</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)

url ="https://colab.research.google.com/drive/14rDFfnBarkB6y7GX9fEEd2Jtstp858L3"
if st.button('Model'):
        webbrowser.open_new_tab(url)

st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
st.markdown("<h6 style='color: skyblue;'>Description: </h6>", unsafe_allow_html=True)
st.write("The objective is to develop a reliable and efficient method for object counting and localization in the inventory using vision interface."
         "Firstly, the Region of interest (ROI) is extracted from the image of inventory using visual features i.e. stable regions of input image."
        "For this, a real time inventory monitoring system using Convolutional Neural Network (CNN) has been proposed"
        "We use CNN  for image recognition and for inventory management MySQL was used in conjunction with streamlit to create our API.")

rad =st.sidebar.radio("Navigation",["Home","UpdateInventory","BuyProducts","Predict"])

if rad == "Home":
    homenew.homexec()

if rad == "UpdateInventory":
    update.updateinv()

if rad == "BuyProducts":
    buy.buyinv()

if rad == "Predict":
    predict.final()