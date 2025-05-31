# app.py
!pip install tensorflow

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Carrega seu modelo salvo (ajuste o caminho)
model = tf.keras.models.load_model('meu_modelo.keras')

# Define as classes
class_names = ['Cat', 'Dog']

# Função para pré-processar a imagem para o modelo (exemplo: resize e escala)
def preprocess_image(image: Image.Image):
    IMG_SIZE = (224, 224)  # ajuste conforme seu modelo
    image = image.resize(IMG_SIZE)
    image = np.array(image) / 255.0
    if image.shape[-1] == 4:  # remover alpha se existir
        image = image[..., :3]
    image = np.expand_dims(image, axis=0)  # batch dimension
    return image

def main():
    st.title("Classificador Cães vs Gatos")

    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_column_width=True)
        
        input_arr = preprocess_image(image)
        prediction = model.predict(input_arr)[0][0]
        
        # Como é binário, assumindo saída sigmoid
        if prediction > 0.5:
            st.success(f"Predição: {class_names[1]} (Confiança: {prediction:.2f})")
        else:
            st.success(f"Predição: {class_names[0]} (Confiança: {1 - prediction:.2f})")

if __name__ == "__main__":
    main()
