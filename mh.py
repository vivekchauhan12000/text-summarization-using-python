import streamlit as st
from gensim.summarization import summarize

#title
st.title("Text summarization")

#textbox
rawtext = st.text_area("enter text")

#button
if st.button("summarize"):
  summarize_result = summarize(rawtext)
  st.success(summarize_result)