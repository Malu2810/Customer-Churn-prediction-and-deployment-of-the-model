# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:27:27 2023

@author: computer
"""

import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users/computer/OneDrive/Desktop/Sunbasedata/churn_model.sav','rb'))
input_data=(63,0,0,17,73.36,236)
as_numpy=np.asarray(input_data)
as_reshape=as_numpy.reshape(1,-1)
prediction=loaded_model.predict(as_reshape)
print(prediction)
if(prediction[0]==0):
  print("No customer churn")
else:
  print("Customer churn")