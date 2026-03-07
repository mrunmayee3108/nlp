import streamlit as st 
import pickle 

st.set_page_config(page_title="Emotion Detection", page_icon="😃", layout="wide")
st.title("Text to Emotion detector")

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

emotion_map = {
    0: "sadness", 
    1: "anger", 
    2: "love", 
    3: "surprise", 
    4: "fear", 
    5: "joy"
}

text = st.text_area("Enter a sentence")

if st.button("Predict Emotion"):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)[0]
    st.success(f"Predicted Emotion: {emotion_map[pred]}")

