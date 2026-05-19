import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="CBSE Study Buddy", layout="wide")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("📚 CBSE Study Buddy")
subject = st.selectbox("Subject", ["Math", "Physics", "Chemistry", "Biology"])
chapter = st.text_input("Chapter Name")

if st.button("Generate Notes"):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Give Class 12 CBSE notes for {subject} - {chapter}. Include key points, solved examples, and 5 PYQs."
    response = model.generate_content(prompt)
    st.markdown(response.text)
