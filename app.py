import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache
def load_iris():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df,target_name = load_iris()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", 0.0, 10.0, 5.0)
sepal_width = st.sidebar.slider("Sepal Width", 0.0, 10.0, 3.0)
petal_length = st.sidebar.slider("Petal Length", 0.0, 10.0, 4.0)
petal_width = st.sidebar.slider("Petal Width", 0.0, 10.0, 1.0)

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
predicted_species = target_name[prediction][0]

st.write(f"Predicted Iris Species: {predicted_species}")