# Core Pkgs
import streamlit as st

# NLP Pkgs
from textblob import TextBlob
import spacy
import neattext as nt

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
# only use if necessae=ry
# matplotlib.use("Agg")
from wordcloud import WordCloud

# main procedure
def main():
    """NLP Web App with Streamlit"""

    st.title("NLP Web App")

    # sidebar menu
    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu", activity)

    # menu options
    if choice == "Text Analysis":
        st.subheader("Text Analysis")
        st.write("")

    if choice == "Translation":
        st.subheader("Translation")
        st.write("")

    if choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        st.write("")

    if choice == "About":
        st.subheader("About")
        st.write("")

        st.markdown("""
           ### NLP Web App made with Streamlit

           for info:
           - [streamlit](https://streamlit.io)         
        """)

if __name__ == "__main__":
    main()

