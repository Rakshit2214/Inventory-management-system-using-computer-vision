import streamlit as st
from dbintegration import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def homexec():
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
    
