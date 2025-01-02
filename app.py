import streamlit as st

st.title('Mi Primera Aplicación en Streamlit')

st.title('Estudiante: ANDRES ABAD NIETO')

# Agregar un texto en la barra lateral
st.sidebar.write("Menú lateral")

# Input de Edad
edad = st.sidebar.number_input("¿Cuál es tu edad?", min_value=0, max_value=120, step=1)

# Input de texto de Nombre
nombre = st.text_input("Ingresa tu nombre:")

# Slider para seleccionar los meses (1 a 12)
mes = st.sidebar.slider("Selecciona un mes:", min_value=1, max_value=12, step=1)

# Checkbox de términos y condiciones
aceptar = st.checkbox("Acepto los términos y condiciones")

# Radio buttons de género
opcion = st.sidebar.radio(
    "Selecciona tu género:",
    ("Masculino", "Femenino")
)

# Select box de países
opcion = st.sidebar.selectbox(
    "Selecciona tu país:",
    ["Colombia", "Ecuador", "Perú", "Argentina"]
)

# File uploader
archivo = st.file_uploader("Sube un archivo", type=["txt", "csv", "xlsx"])

# Input de fecha selector
fecha = st.date_input("Selecciona una fecha:")

# Input de hora
hora = st.time_input("Selecciona una hora:")

# Botón enviar
if st.button("Enviar Información"):
    st.write("¡El formulario ha sido enviado!")