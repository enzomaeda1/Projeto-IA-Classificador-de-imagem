# 🐱🐶 Classificação de Imagens de Gatos e Cachorros com Deep Learning
Este projeto tem como objetivo construir um modelo de rede neural profunda capaz de classificar imagens entre gatos e cachorros com alta precisão. Utilizando técnicas modernas de deep learning e transferência de aprendizado, alcançamos ótimos resultados em validação e teste.

## Link do aplicativo Streamlit
https://projeto-ia-classificador-de-imagem-vuibtqtccwfdmhvfqercvf.streamlit.app/

## Link do video do Youtube
https://www.youtube.com/watch?v=EwU4xmixejc&ab_channel=EnzoMaeda

# 📁 Dataset
## Fonte: Kaggle - Cats and Dogs

## O dataset contém imagens divididas em duas pastas:

* train/ — imagens de treino

* val/ — imagens de validação

* As imagens estão classificadas em subpastas Cat/ e Dog/.

# 🛠️ Ferramentas e Bibliotecas
* Python 3.12+

* TensorFlow/Keras

* Matplotlib

* NumPy

* Streamlit (opcional para visualização)

# 🧠 Arquitetura do Modelo
Modelo base: MobileNetV2 pré-treinado na ImageNet

## Camadas adicionais:

* GlobalAveragePooling2D

* Dropout

* Dense (camada de saída com ativação sigmoid)

# ⚙️ Treinamento
* Função de perda: binary_crossentropy

* Otimizador: Adam (learning_rate=0.0001)

## Técnicas utilizadas:

* Data Augmentation com ImageDataGenerator

* EarlyStopping para evitar overfitting

## Precisão final:

* Validação: 97%

* Teste: 98%

* As perdas durante o treinamento foram mínimas, o que mostra estabilidade e generalização.

* 💡 Observação: Não foi necessário realizar fine tuning completo, pois o modelo já apresentava ótima performance com o congelamento parcial da base MobileNetV2.

# 📊 Resultados

## Gráficos de perda e acurácia ao longo das épocas

![image](https://github.com/user-attachments/assets/cbc199f5-9d8e-4665-9e71-4af4134ec466)


## Visualização de imagens de validação com as previsões do modelo

![image](https://github.com/user-attachments/assets/147df6ee-1c9d-4ab6-9372-147f9cfc49f7)

![image](https://github.com/user-attachments/assets/328678a1-121f-4691-a9bc-0e2b64b0ad25)

# Aplicativo Streamlit

Foi feito um aplicativo Streamlit onde o usuário pode testar o modelo com imagens de cães e gatos

![image](https://github.com/user-attachments/assets/ad6f976a-9af1-41fb-8792-de5c44a1f538)


