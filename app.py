import streamlit as st
import matplotlib.pyplot as plt 
import streamlit.components.v1 as components


from analysis.algo import data



# Sidebar
st.sidebar.header("Menu")




# Body
if st.button("Data"):
    st.dataframe(data['data_set'])


if st.button("Data Describe"):
    st.dataframe(data['data_describe'])
    
if st.button("Correlation Matrix"):
        st.image("/Users/iamsan/Desktop/py_data/images/plot1.png")
if st.button("Histogram"):
    st.image("/Users/iamsan/Desktop/py_data/images/histo.png", width=850)
    


