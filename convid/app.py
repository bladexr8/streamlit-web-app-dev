import streamlit as st
st.set_page_config(page_title="Covid19 Detection Tool", page_icon="covid19.jpeg", layout='centered', initial_sidebar_state='auto')

import os
import time

# Viz Pkgs
import cv2
from PIL import Image, ImageEnhance
import numpy as np

# AI Pkgs
import tensorflow as tf

def main():
    """Simple Tool for Convid Detection from Chest X-Ray"""
	
    html_templ = """
	<div style="background-color:blue;padding:10px;">
	<h1 style="color:yellow">Convid Detection Tool</h1>
	</div>
	"""
    st.markdown(html_templ,unsafe_allow_html=True)
    st.write("A simple proposal for Convid misdiagnosis powered by Deep Learning and Streamlit")

    st.sidebar.image("Images/covid19.jpeg",width=300)

    image_file = st.sidebar.file_uploader("Upload an X-Ray Image (jpg, png or jpeg)",type=['jpg','png','jpeg'])

    if image_file is not None:
        our_image = Image.open(image_file)

        if st.sidebar.button("Image Preview"):
            st.sidebar.image(our_image,width=300)

        activities = ["Image Enhancement","Diagnosis", "Disclaimer and Info"]
        choice = st.sidebar.selectbox("Select Activty",activities)

        if choice == 'Image Enhancement':
            st.subheader("Image Enhancement")

            enhance_type = st.sidebar.radio("Enhancement Type", ["Original", "Contrast", "Brightness"])

            if enhance_type == "Contrast":
                  c_rate = st.slider("Contrast", 0.5, 5.0)
                  enhancer = ImageEnhance.Contrast(our_image)
                  img_output = enhancer.enhance(c_rate)
                  st.image(img_output, width=600, use_container_width=True)

            elif enhance_type == "Brightness":
                  c_rate = st.slider("Brightness", 0.5, 5.0)
                  enhancer = ImageEnhance.Brightness(our_image)
                  img_output = enhancer.enhance(c_rate)
                  st.image(img_output, width=600, use_container_width=True)
            else:
                  st.text("Original Image")
                  st.image(our_image, width=600, use_container_width=True)
            
        elif choice == 'Diagnosis':
            if st.sidebar.button("Diagnosis"):
                new_img = np.array(our_image.convert('RGB')) #our image is converted into an array
                new_img = cv2.cvtColor(new_img,1) #0 is original, 1 is grayscale
                gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
                st.text("Chest X-Ray")
                st.image(gray, width=400, use_container_width=True)

                #X-Ray Imge Pre-processing
                IMG_SIZE = (200, 200)
                img = cv2.equalizeHist(gray)
                img = cv2.resize(img, IMG_SIZE)
                img = img/255 #normalization

                # Image reshaping according to tensorflow format
                X_Ray = img.reshape(1, 200, 200, 1)

                #Pre-trained CNN Model loading
                model = tf.keras.models.load_model("./models/Covid19_CNN_Classifier.h5")

                #Diagnosis (Prediction== Binary Classification)
                diagnosis_proba = model.predict(X_Ray)
                diagnosis = np.argmax(diagnosis_proba,axis=1)

                my_bar = st.sidebar.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.05)
                    my_bar.progress(percent_complete + 1)

				#Diagnosis Cases: No-Covid=0, Covid=1
                if diagnosis == 0:
                    st.sidebar.success("DIAGNOSIS: NO COVID-19")
                else:
                    st.sidebar.error("DIAGNOSIS: COVID-19")

                st.warning("CONVID doesn't exist! This Web App is just a DEMO about Streamlit and Artificial Intelligence and there is no clinical value in its diagnosis!")

        else:
            st.subheader("Disclaimer and Info")
            st.write("This App is just a Demo. It does not provide any medical advice")
            st.write("P.S. Convid doesn't exist")

    if st.sidebar.button("About the Author"):
        st.sidebar.subheader("Convid Detection Tool")
        st.sidebar.markdown("by [Author's Name](https://www.authorswebsite.com)")
        st.sidebar.markdown("[author@gmail.com](mailto:author@gmail.com)")
        st.sidebar.text("All Rights Reserved (2023)")


if __name__ == '__main__':
		main()	