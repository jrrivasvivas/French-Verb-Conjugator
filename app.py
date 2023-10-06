import streamlit as st
import random
from src.conjugador import ConjugadorFrances

# Lista de verbos en francés (puedes cargarla desde un archivo si es necesario)
verbos_frances = ["manger", "parler", "aller", "boire", "prendre", "venir"]

# Lista de pronombres personales en francés
pronombres = ["je", "tu", "il/elle/on", "nous", "vous", "ils/elles"]

# Función para seleccionar un verbo y un pronombre al azar
def seleccionar_ejercicio():
    verbo = random.choice(verbos_frances)
    pronombre = random.choice(pronombres)
    return verbo, pronombre

conjugador = ConjugadorFrances()

# Función principal para la aplicación
def main():
    st.title("Conjugador de Verbos en Francés")
    
    # Bandera para controlar si el ejercicio se ha generado
    ejercicio_generado = False

    # Botón para comenzar un nuevo ejercicio
    if st.button("Nuevo ejercicio"):
        # Generar el ejercicio solo si no se ha generado previamente
        if not ejercicio_generado:
            verbo, pronombre = seleccionar_ejercicio()
            ejercicio_generado = True
        else:
            st.warning("Ya hay un ejercicio en curso. Verifica antes de generar uno nuevo.")
            return
        
        respuesta_usuario = st.text_input(f"Conjugue el verbo '{verbo}' para '{pronombre}':")
        
        # Crear un contenedor para mostrar la retroalimentación
        resultado_container = st.empty()

        # Verificar la respuesta del usuario solo cuando hace clic en "Verificar"
        if st.button("Verificar"):
            if verificar_respuesta(verbo, pronombre, respuesta_usuario):
                resultado_container.success("¡Correcto!")
            else:
                resultado_container.error("Incorrecto. La respuesta correcta es ...")  # Aquí muestra la respuesta correcta

if __name__ == "__main__":
    main()
