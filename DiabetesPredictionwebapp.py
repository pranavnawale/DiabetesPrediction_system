# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:01:23 2022

@author: Pranav
"""

import numpy as np

import streamlit as st
import pickle as pickle

#loading the saved model
loaded_model=pickle.load(open("C:/Users/Pranav/trained_model.sav",'rb'))

def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      print('The person is not diabetic')
    else:
      print('The person is diabetic')
      
     
def main():
    #giving the title
    st.title('Diabetes Prediction Web App')

    #getting the input data fron the user
    
    Pregnancies=st.text_input('Number Of Pregnabcies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('BloodPressure Value')
    SkinThicknes=st.text_input('SkinThicknes Value')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI Value')
    DiabetesPedigree=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age Of The Person')
    
    #code for Prediction
    diagnosis= ''
    
    #creating the a button for predction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThicknes,Insulin,BMI,DiabetesPedigree,Age])
    
    
    st.success(diagnosis)

    
if __name__=='__main__':
    main()
