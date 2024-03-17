import streamlit as st
from deep_translator import GoogleTranslator
import requests

API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

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
