from turtle import width
import streamlit as st
from dbintegration import *
import homenew
import plotly.graph_objects as go
import matplotlib.pyplot as plt

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
    

def updateinv() :
    
    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: white;'>Update Inventory : </h3>", unsafe_allow_html=True)
    newsize = (500, 500)

    from PIL import Image
    image1 = Image.open('products/milk.jpeg')
    image1 = image1.resize(newsize)
    image2 = Image.open('products/nuts.jpeg')
    image2 = image2.resize(newsize)
    image3 = Image.open('products/oil.jpeg')
    image3 = image3.resize(newsize)
    image4 = Image.open('products/soda.jpeg')
    image4 = image4.resize(newsize)
    image5 = Image.open('products/tea.jpeg')
    image5 = image5.resize(newsize)

    # cnt = st.slider(" ", 0, 15, 10)
    # st.write("Buy ",cnt," milk packets : Price = ")
    

    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([3, 1, 3, 1, 3])
    
    col1.markdown("<h4 style='text-align: center; color: white;'>Milk</h4>", unsafe_allow_html=True)
    col1.image(image1, use_column_width = True)
    count1 = col1.slider(" ", 0, 15, 0,key=1)
    col1.write("Count :")
    col1.write(count1)

    col3.markdown("<h4 style='text-align: center; color: white;'>Nuts</h4>", unsafe_allow_html=True)
    col3.image(image2, use_column_width = True)
    count3 = col3.slider(" ", 0, 15, 0,key=3)
    col3.write("Count :")
    col3.write(count3)

    col5.markdown("<h4 style='text-align: center; color: white;'>Oil</h4>", unsafe_allow_html=True)
    col5.image(image3, use_column_width = True)
    count5 = col5.slider(" ", 0, 15, 0,key=5)
    col5.write("Count :")
    col5.write(count5)

    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: white;</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([1, 3, 1, 3, 1])

    col2.markdown("<h4 style='text-align: center; color: white;'>Soda</h4>", unsafe_allow_html=True)
    col2.image(image4, use_column_width = True)
    count2 = col2.slider(" ", 0, 15, 0,key=2)
    col2.write("Count :")
    col2.write(count2)

    col4.markdown("<h4 style='text-align: center; color: white;'>Tea</h4>", unsafe_allow_html=True)
    col4.image(image5, use_column_width = True)
    count4 = col4.slider(" ", 0, 15, 0,key=4)
    col4.write("Count :")
    col4.write(count4)
    pname=['MILK',"NUTS","OIL","SODA","TEA"]
    clist = [count1,count3,count5,count2,count4]
    
    if(st.button("Proceed")):
        updatevals(pname,clist)
        st.warning('Inventory has been updated')
        checkup()
        



    

