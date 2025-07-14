import streamlit as st

st.title("Hello ThinkRook Chatbot :)")
st.caption("Welcome to your first chatbot app !!")

user_input = st.text_input("Say Something To ThinkRook Bot")

if user_input:
    st.write("You said:", user_input)
    st.write("ThinkRook bot says, Hello there!!")