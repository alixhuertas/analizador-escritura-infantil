import streamlit as st
from PIL import Image
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

st.title("✏️ Analizador de Escritura Infantil")

st.write(
    "Sube una imagen de un cuaderno para analizar la escritura."
)

@st.cache_resource
def cargar_modelo():
    processor = TrOCRProcessor.from_pretrained(
        "microsoft/trocr-base-handwritten"
    )

    model = VisionEncoderDecoderModel.from_pretrained(
        "microsoft/trocr-base-handwritten"
    )

    return processor, model

archivo = st.file_uploader(
    "Sube una imagen",
    type=["jpg", "jpeg", "png"]
)

if archivo:

    imagen = Image.open(archivo).convert("RGB")

    st.image(
        imagen,
        caption="Imagen cargada"
    )

    with st.spinner("Analizando escritura..."):

        processor, model = cargar_modelo()

        pixel_values = processor(
            images=imagen,
            return_tensors="pt"
        ).pixel_values

        with torch.no_grad():
            generated_ids = model.generate(pixel_values)

        texto = processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

    st.subheader("Texto detectado")
    st.write(texto)
