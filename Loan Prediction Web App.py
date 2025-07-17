# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 19:39:50 2025

@author: syeme
"""

import pickle
import numpy as np
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open("C:/Users/syeme/Downloads/Machine Learning/Project 4 - Loan Prediction/trained_model.sav", 'rb'))

def loan_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    result = loaded_model.predict(input_data_reshaped)
    
    return "Approved" if result == 1 else "Not Approved"

def main():
    st.title("Loan Approval Prediction")
    
    Gender = 1 if st.selectbox("Select Gender", ["Male", "Female"]) == "Male" else 0
    Married = 1 if st.selectbox("Married", ["Yes", "No"]) == "Yes" else 0
    Dependents = st.selectbox("Dependents Count", [0,1, 2, "3+"])
    Dependents = 4 if Dependents == "3+" else Dependents
    
    Education = 1 if st.selectbox("Education", ["Graduate", "Not Graduate"]) == "Graduate" else 0
    Self_Employed = 1 if st.selectbox("Self Employed",["Yes","No"]) == "Yes" else 0
    ApplicantIncome = st.number_input("Enter Applicant Income",step=0.1, format="%.1f")
    CoapplicantIncome = st.number_input("Enter Coapplicant Income", step=0.1, format="%.1f")
    LoanAmount = st.number_input("Enter Loan Amount", step=0.1, format="%.1f")
    Loan_Amount_Term = st.number_input("Enter Loan Term", step=0.1, format="%.1f")
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    Property_Area = st.selectbox("Property Area", ["Rural","Semi Urban", "Urban"])
    
    if(Property_Area=="Rural"):
        Property_Area=0
    elif(Property_Area=="Semi Urban"):
        Property_Area=1
    else:
        Property_Area=2
    
    if st.button("Loan Check"):
        output = loan_prediction([
            Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome,
            CoapplicantIncome, LoanAmount, Loan_Amount_Term,
            Credit_History, Property_Area
        ])
        st.success(f"Loan Status: {output}")

if __name__ == '__main__':
    main()
