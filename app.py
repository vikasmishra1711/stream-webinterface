import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}! Welcome to Streamlit.")