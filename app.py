import streamlit as st
import numpy as np
from tensorflow import keras
from PIL import Image

model = keras.models.load_model("cifar10_cnn_model.keras")

class_names = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

st.title("CIFAR-10 Image Classifier")

uploaded_file = st.file_uploader("Upload a CIFAR-10 image (32x32)", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((32,32))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_array = np.array(image).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    score = predictions[0]
    predicted_class = class_names[np.argmax(score)]

    st.write(f"### Prediction: **{predicted_class}**")
    st.write("Confidence Scores: ")
    for i, prob in enumerate(score):
        st.write(f"{class_names[i]}: {prob:.4f}")