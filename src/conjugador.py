from textblob import TextBlob

class ConjugadorFrances:
    def __init__(self):
        pass

    def verificar_conjugacion(self, verbo, pronombre, respuesta_usuario):
        """
        Verifica si la respuesta del usuario coincide con la conjugación correcta.
        Args:
            verbo (str): El verbo en infinitivo.
            pronombre (str): El pronombre personal.
            respuesta_usuario (str): La respuesta del usuario.

        Returns:
            bool: True si la respuesta es correcta, False en caso contrario.
        """
        # Crear un objeto TextBlob con el verbo en infinitivo
        verbo_blob = TextBlob(verbo)

        # Conjugamos el verbo en función del pronombre personal
        conjugacion_correcta = verbo_blob.conjugate(pronoun=pronombre)

        # Convertir la conjugación correcta a minúsculas y quitar espacios
        conjugacion_correcta = conjugacion_correcta.lower().replace(" ", "")

        # Convertir la respuesta del usuario a minúsculas y quitar espacios
        respuesta_usuario = respuesta_usuario.lower().replace(" ", "")

        # Verificar si la respuesta del usuario coincide con la conjugación correcta
        return respuesta_usuario == conjugacion_correcta
    
# Ejemplo de uso (fuera de la clase)
if __name__ == "__main__":
    # Crear una instancia del conjugador
    conjugador = ConjugadorFrances()

    # Verbo, pronombre y respuesta del usuario para el ejemplo
    verbo = "manger"
    pronombre = "tu"
    respuesta_usuario = "manges"

    # Verificar si la respuesta del usuario es correcta
    es_correcto = conjugador.verificar_conjugacion(verbo, pronombre, respuesta_usuario)

    # Mostrar resultado
    if es_correcto:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es: {conjugacion_correcta}")
