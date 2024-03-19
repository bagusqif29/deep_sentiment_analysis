import streamlit as st
from deep_translator import GoogleTranslator
import requests
import os

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

API_TOKEN = st.secrets["API_TOKEN"]
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = st.secrets["api_url"]

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()



st.title('Sentiment Analysis with DeepLearning')

user_input = st.text_input("Enter Your Sentence :")
if user_input :
    translated_text = GoogleTranslator(source='auto', target='english').translate(user_input)
    data = query({"inputs": translated_text})
    data = data[0]

    if data[0]['score'] < data[1]['score']:
        data_f = data[1]
    elif data[0]['score'] >= data[1]['score']:
        data_f = data[0]
    else:
        data_f = 'unknown'

        
    st.write('  ')
    st.title(data_f['label'])
