import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

model = tf.keras.models.load_model('model.h5')

with open('label_encode_gender.pkl','rb') as file:
    label_encode_gender = pickle.load(file)
    
with open('one_hot_encode_geography.pkl','rb') as file:
    one_hot_encoder_geography = pickle.load(file)
    
with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)
    
st.title('Customer Churn Prediction')

#User input
geography = st.selectbox('Geography',one_hot_encoder_geography.categories_[0])
gender = st.selectbox('Gender',label_encode_gender.classes_)
age = st.slider('Age',18,100)
balance = st.number_input('Balance',min_value=0.0)
credit_score = st.number_input('Credit Score',min_value=0)
estimated_salary = st.number_input('Estimated Salary',min_value=0)
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number of Products',1,4)
has_cr_card = st.selectbox('Has Credit Card',[0,1])
is_active_member = st.selectbox('Is Active Member',[0,1])

input_data = pd.DataFrame({
    'CreditScore':[credit_score],
    'Gender':[label_encode_gender.transform([gender])[0]],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary]
})

#One hot encode Geography
geo_encoded = one_hot_encoder_geography.transform([[geography]]).toarray()
geography_df = pd.DataFrame(geo_encoded, columns=one_hot_encoder_geography.get_feature_names_out(['Geography']))
input_data = pd.concat([input_data.reset_index(drop=True),geography_df], axis=1)

input_data_scaled = scaler.transform(input_data)

prediction = model.predict(input_data_scaled)
prediction_probability = prediction[0][0]

if prediction_probability > 0.5:
    st.write(f'Prediction Probability: {prediction_probability:.2f}, The customer is likely to churn.')
else:
    st.write(f'Prediction Probability: {prediction_probability:.2f}, The customer is not likely to churn.')