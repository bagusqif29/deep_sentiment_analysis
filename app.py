import streamlit as st
from deep_translator import GoogleTranslator
import requests
import os
from flask_sqlalchemy import SQLAlchemy


st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# Inisialisasi database
db = SQLAlchemy('sqlite:///example.db')  # Ganti dengan URL database Anda

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(3200), nullable=False)
    text_trans_en = db.Column(db.String(3200))
    text_trans_id = db.Column(db.String(3200))
    origin_lang = db.Column(db.String(100))
    sentiment = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    long = db.Column(db.String(100))
    lat = db.Column(db.String(100))
    city = db.Column(db.String(100))
    waktu = db.Column(db.DateTime, default=db.func.current_timestamp())

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

        
    st.write('   ')
    st.title(data_f['label'])
