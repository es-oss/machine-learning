# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:15:01 2021

@author: siddhardhan
"""

import numpy as np
import joblib
import streamlit as st


 
    
  
def main():
    
    
    st.title('insurance predict')

    model = joblib.load('model_joblib_gr')

    p1 = st.slider('Enter your age',18,100)

    s1 = st.selectbox('sex',('male','female'))

    if s1=='male':
        p2=1
    else:
        p2=0

    p3 = st.number_input('Enter your BMI value')

    p4 = st.slider('Enter Number Of Childern',0,4)

    s2 = st.selectbox("Smoker",("yes","no"))

    if s2=='yes':
        p5=1
    else:
        p5=0  

    p6 = st.slider('Enter your Region',1,4)   

    if st.button('predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6]])

        st.balloons()

        
        st.success('your insurance cost {}'.format(round(pred[0],2)))

           
      
    
    
    
if __name__ == '__main__':
    main()