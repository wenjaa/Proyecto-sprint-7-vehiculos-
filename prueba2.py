import streamlit as st

# Título de la app
st.title("Mi Primera Aplicación Streamlit")

# Caja de texto para que el usuario ingrese su nombre
nombre = st.text_input("Escribe tu nombre:")

# Mostrar el texto ingresado
if nombre:
    st.write(f"¡Hola, {nombre}!")
else:
    st.write("Por favor, ingresa tu nombre.")