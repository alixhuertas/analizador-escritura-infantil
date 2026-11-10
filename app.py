
import streamlit as st

st.title("✏️ Analizador de Escritura Infantil")

st.write(
    "Bienvenido. Aquí podrás subir una imagen de un cuaderno para analizar la escritura."
)

archivo = st.file_uploader(
    "Sube una imagen",
    type=["jpg", "jpeg", "png"]
)

if archivo:
    st.image(archivo, caption="Imagen cargada")
    st.success("Imagen recibida correctamente")
