import streamlit as st

# render text levels
st.title("Streamlit Basics")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")
st.write("This is a write dimension")

# render markdown and html
st.markdown("[Streamlit](https://www.streamlit.io)")
html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

# render messages
st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

# display an image
from PIL import Image
img = Image.open("packt.jpeg")
st.image(img, width=300, caption="Packt Logo")

# display a video
video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

# display video from a url
st.video("https://www.youtube.com/watch?v=q2EqJW8VzJo")

# display an audio file
audio_file = open("sample1.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.header("Widgets")

# display a button
if st.button("Play"):
    st.text("Hello World!")

# display a checkbox
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")

# radio button
radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == 'A':
    st.info("You selected A")
else:
    st.info("You selected B")

# select box
city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

# multi-select box
occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

# text input
name = st.text_input("Your Name", "Write something...")
st.text(name)

# number input
age = st.number_input("Input a number")

# text area
message = st.text_area("Your Message", "Write something...")

# slider
select_val = st.slider("Select a Value", 1, 10)

# date/time widget
import datetime
today = st.date_input("Today is ", datetime.datetime.now())

# time
import time
hour = st.time_input("This time is", datetime.time(12,30))

# balloon
if st.button("Balloons"):
    st.balloons()

# pandas dataframe
st.header("Dataframes and Tables")
import pandas as pd
df = pd.read_csv("auto.csv")
st.dataframe(df.head(10))

# table
st.table(df.head(10))

# area chart
st.area_chart(df[["mpg", "cylinders"]])

# bar chart
st.bar_chart(df[["mpg", "cylinders"]].head(20))

# line chart
st.line_chart(df[["mpg", "cylinders"]].head(20))

# use python libraries for plotting
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[["mpg", "cylinders", "displacement"]].corr(), annot=True)
st.pyplot(fig)

# render json
data = {"name":"John","surname":"Wick"}
st.json(data)

# render code
st.code("import pandas as pd")

# progress bar
my_bar = st.progress(0)
for value in range(100):
    time.sleep(0.1)
    my_bar.progress(value + 1)

# spinner
with st.spinner("Please wait..."):
    time.sleep(10)
st.success("Done!")

