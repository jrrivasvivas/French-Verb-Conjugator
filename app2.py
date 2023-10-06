import streamlit as st
import random

# Lista de verbos en francés y pronombres personales en francés
verbos_frances = ["manger", "parler", "aller"]
pronombres = ["je", "tu", "il/elle/on"]

# Función para seleccionar un verbo y un pronombre al azar
def seleccionar_ejercicio():
    verbo = random.choice(verbos_frances)
    pronombre = random.choice(pronombres)
    return verbo, pronombre

# Función para verificar la respuesta del usuario
def verificar_respuesta(verbo, pronombre, respuesta_usuario):
    conjugacion_correcta = f"{verbo}{'e' if pronombre == 'je' else 'es'}"
    return respuesta_usuario.lower() == conjugacion_correcta

# Función principal para la aplicación
def main():
    st.title("Conjugador de Verbos en Francés")
    
    # Generar un nuevo ejercicio
    verbo, pronombre = seleccionar_ejercicio()
    respuesta_usuario = st.text_input(f"Conjugue el verbo '{verbo}' para '{pronombre}':")
    
    # Verificar la respuesta del usuario
    if st.button("Verificar"):
        if verificar_respuesta(verbo, pronombre, respuesta_usuario):
            st.success("¡Correcto!")
        else:
            st.error("Incorrecto. La respuesta correcta es ...")  # Aquí muestra la respuesta correcta

if __name__ == "__main__":
    main()
