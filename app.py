import uuid
import streamlit as st

from analysis.algo import data
from ui.login import login
from ui.model_ui import model_ui




loggedInUser = None

st.beta_set_page_config(
    page_title=("Project X"), 
    layout = "centered"
    
)


user_details = [
            {
                "id" : uuid.uuid4(),
                 "username" : "test1", 
                 "password" : "pass"
                
            }, 
            {
                "id" : uuid.uuid4(),
                "username" : "test2",
                "password" : "pass2"
            }
        ]



st.title("XYZ Application")
isLoggedIn = False
sidebar_selection = st.sidebar.selectbox("Choose Your Operation", ["About WebApp", "Login", "Sign Up"])


if sidebar_selection == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type = "password")
    if st.sidebar.checkbox("Login"):
        for item in user_details:
            if username == item['username'] and password == item['password']:
                
                navigation = st.selectbox("How can we help you today ?",
                                               
                            ["Choose Options", "View Data", "Visualize Data", "Predict", "Results",
                             
                             "Check"])
                if navigation == "Choose Options":
                    st.text("Please choose an operation from the list.")
                if navigation == "View Data":
                    st.header("Data Set")
                    st.text("This is sample dataset obtained from ")
                    st.dataframe(data['data_set'])
                    
elif sidebar_selection == "Sign Up":
    username = st.text_input("Enter Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type = "password")
    if username == "" or password == "":
            st.warning("Username or password cannot be blank")
    else:
        user_details.append({
            "id" : uuid.uuid4(),
            "username" : username,
            "password": password})
        st.success("Sign up successful!")
        
elif sidebar_selection == "About WebApp":
    st.text("This application will predict heart disease")
        



#st.write("LOGIN")
#isLoggedIn = False

#if isLoggedIn is False:
 #   needLogIn = login()
 #   isLoggedIn = True
##else:
 #   st.write("Please Login")

#if isLoggedIn is True:
 #   needLogIn = None'''