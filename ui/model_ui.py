#!/usr/bin/env python3

import streamlit as st
from analysis.algo import data

'''

xdata = {
      "data_set" : data_set ,
      "data_info" : data_set.info(),
      "data_describe" : data_set.describe(),
      "data_histo" : visualization_correlation_matrix()
        
  } 


'''

def model_ui():
    choices = ["Data", "Visualization", "Prediction", "Results"]
    radio = st.sidebar.radio("Menu", options= choices)
    
    if radio == "Data":
        st.title("Data Set")
        st.text("Sample dataset used for analyis. Source : this and that")
        st.dataframe(data['data_set'])
    if radio == "Visualization":
        st.write("Visualization")
   
    
