# analizador-escritura-infantil
import streamlit as st

st.title("✏️ Analizador de Escritura Infantil")

archivo = st.file_uploader(
    "Sube una imagen del cuaderno",
    type=["jpg", "jpeg", "png"]
)

if archivo:

    st.image(
        archivo,
        caption="Imagen cargada",
        use_container_width=True
    )

    st.subheader("Texto detectado")

    texto_detectado = """
Bolita de nieve era un cordero que tenía muchos amigos.
El lobo quería comerlo.
"""

    st.write(texto_detectado)

    st.subheader("Posibles errores encontrados")

    st.warning("queria → quería (falta tilde)")
    st.warning("tenia → tenía (falta tilde)")

    st.success("Análisis finalizado")
