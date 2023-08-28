# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:28:36 2023

@author: computer
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('C:/Users/computer/OneDrive/Desktop/Sunbasedata/churn_model.sav','rb'))
def churn_pred(input_data):
    
    as_numpy=np.asarray(input_data)
    as_reshape=as_numpy.reshape(1,-1)
    prediction=loaded_model.predict(as_reshape)
    print(prediction)
    if(prediction[0]==0):
       return "No customer churn"
    else:
        return "Customer churn"

def main():#Age  Gender  Location  Subscription_Length_Months  Monthly_Bill Total_Usage_GB
    st.title("Customer Churn Prediction App:")
    Age=st.text_input("Age:")
    Gender=st.text_input("Gender(Male:1 Female:0):")
    Location=st.text_input("Location:")
    Subscription_Length_Months=st.text_input("Number of months of subscription:")
    Monthly_Bill=st.text_input("Monthly bill:")
    Total_Usage_GB=st.text_input("Total usage(in GB):")

    find=''
    if st.button("Find"):
        find=churn_pred([Age,Gender,Location,Subscription_Length_Months,Monthly_Bill,Total_Usage_GB])
    st.success(find)
if __name__ == '__main':
    main()