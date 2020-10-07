
import uuid
import csv

import streamlit as st
import pandas as pd

from streamlit.components.v1 import html 
from analysis.algo import data




loggedInUser = None

st.beta_set_page_config(
    page_title=("MITS 6500"), 
    layout = "centered"
    
)

user_details = [
            {
                "id" : uuid.uuid4(),
                 "username" : "test1", 
                 "password" : "pass",
                 "user_type" : "Admin"
                
            }, 
            {
                "id" : uuid.uuid4(),
                "username" : "test2",
                "password" : "pass",
                "user_type" : "Client"
            }
        ]

columns = """
 <ul>
     <li>Age - Age of an individual</li>
     <li> And so on </li>
 </ul>

"""


st.title("MITS 6500 Heart Disease Prediction Web Application")
isLoggedIn = False
sidebar_selection = st.sidebar.selectbox("Choose Your Operation", ["About WebApp", "Login", "Sign Up"])


if sidebar_selection == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type = "password")
    if st.sidebar.checkbox("Login"):
        for item in user_details:
            if username == item['username'] and password == item['password']:
                if item['user_type'] == "Admin":
                    navigation = st.selectbox("How can we help you today ?",["Choose Options", "View Data", "Visualize Data", "Predict", "Results"])
                    if navigation == "Choose Options":
                        st.text("Please choose an operation from the list.")
                    if navigation == "View Data":
                        st.header("Data Set")
                        st.dataframe(data['data_set'])
                        st.header("Description About the Data")
                        html(columns)
                        st.header("Describe Data")
                        st.dataframe(data["data_describe"]())
                    if navigation == "Visualize Data":
                        st.header("Variation of Age againts each target")
                        st.pyplot(data['target_age']())
                        
                        st.header("Bar Diagram")
                        st.pyplot(data['age_sex_target']())
                    if navigation == "Predict":
                        st.header("Naive Gausian Implementation")
                        st.code("""
                                def nb_implementation():
                                    X = data_set.iloc[:, :-1].values
                                    y = data_set.iloc[:, -1].values
                                    xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.2, random_state = 0)
                                    nb = GaussianNB()
                                    nb.fit(xTrain, yTrain)
                                    yPredict = nb.predict(xTest)
                                    
                                    # Accuracy Score 
                                    cm = confusion_matrix(yTest, yPredict)
                                    accuracy_score(yTest, yPredict)
                                    report = classification_report(yTest, yPredict)
                                    return report
                        """)
                        st.header("Prediction Results")
                        st.code(data['report']())
                    if navigation == "Results":
                        st.header("Please enter your data below")
                        age = st.text_input("Enter Age")
                        sex = st.text_input("Enter Gender")
                        html("<small>Enter 1 for Male and 0 for Female</small>")
                        cp = st.text_input("Enter Chest Pain type")
                        html("<small>Enter 1 - typical angina, 2 - atypical angina, 3 - non-anginal, 4 - asymptotic pain</small>")
                        trestbps = st.text_input("Resting Blood Pressure")
                        chol = st.text_input("Serum Cholestrol")
                        fbs = st.text_input("Fasting Blood Sugar")
                        html("<small>Enter 1 if fasting blood sugar is greater than 120 mg. Enter 0 otherwise")
                        restecg = st.text_input("Resting ECG")
                        html("<small>Enter 0 for normal, 1 having ST-T wave abnormality and 3 for left ventricular hyperthrophy</samll>")
                        thalach = st.text_input("Maximum Heart Rate")
                        exang = st.text_input("Exercise Induced Angina")
                        html("<small>Enter 1 if yes , 0 otherwise</small>")
                        oldpeak = st.text_input("ST induced by exercise")
                        slope = st.text_input("Peak Exercise ST Segment")
                        ca = st.text_input("Number of major vessels")
                        html("<small>Enter major vessels 0-3")
                        thal = st.text_input("Thalassemia Scan Results")
                        html("<small>Enter 3 for normal, 6 for fixed defect and 7 for reversible defect")
                        target = st.text_input("Enter if already suffering from  heart realted  issues")
                        html("<small>Enter 0 for no heart related issues, 1 for if any issues exists")
                        
                        if st.button("Submit"):
                            user_data_df = pd.DataFrame([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target])
                            st.header("User Data Results")
                            # user_report = user_implementation(user_data_df)
                            # st.code(user_report)
                        
                            
                        
                        
                
                    
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
        