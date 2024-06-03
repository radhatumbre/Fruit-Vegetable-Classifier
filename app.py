import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import  load_model
import streamlit as st
import numpy as np 
from PIL import Image

st.header('Image Classification Model')
model = load_model('Image_classify.keras')

data_cat = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower',
            'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi',
            'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate',
            'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip',
            'watermelon']

img_height = 180
img_width = 180

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    resized_image = image.resize((img_height, img_width))
    img_array = tf.keras.utils.img_to_array(resized_image)
    img_bat = tf.expand_dims(img_array, 0)

    predict = model.predict(img_bat)
    score = tf.nn.softmax(predict[0])

    st.write('Veg/Fruit in image is ' + data_cat[np.argmax(score)])
    st.write('With accuracy of ' + str(np.max(score) * 100) + '%')
else:
    st.write("Please upload an image file.")