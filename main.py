import streamlit as st

with open("./README.md", "r") as fp:
    st.markdown(fp.read())
