# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:47:44 2020

@author: ms101
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from pathlib import Path
import pickle

path = Path("C:/Users/ms101/OneDrive/Techlabs_Tracklead/Streamlit Workshop/workshop_base")

diamonds = pd.read_csv(path / "diamonds.csv", index_col=0)

y = diamonds["price"]
X = diamonds.drop(["price","cut","color",
                   "clarity","depth","table"], axis=1)

model = LinearRegression().fit(X,y)

test_data = X.sample(1)

print(model.predict(test_data))

pickle.dump(model,open("model.pkl","wb"))