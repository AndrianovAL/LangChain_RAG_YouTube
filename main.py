
import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(label="Input YouTube URL:", max_chars=50)  # "https://www.youtube.com/watch?v=5MgBikgcWnY"
        query = st.sidebar.text_area(label="Input query:", max_chars=50, key="query")  # query = "What is the main idea of this video?"
        api_key = st.sidebar.text_area(label="Input Google Gemini API key:", max_chars=39)
        submit_button = st.form_submit_button(label='Submit')

if youtube_url and query:
    db = lch.make_vectordb_from_youtube_url(youtube_url)
    if db:
        response, docs = lch.get_response_from_query(db, query, api_key)
        # st.write(response)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=80))
