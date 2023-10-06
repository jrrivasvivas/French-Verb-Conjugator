import sys
from textblob import TextBlob

class ConjugadorFrances:
    def conjugador_blob(self, verbo, pronombre):
        verbo_blob = TextBlob(verbo)
        conjugacion_correcta = verbo_blob.conjugate(pronoun=pronombre).lower()
        return conjugacion_correcta

    def verificar_conjugacion(self, verbo, pronombre, respuesta_usuario):
        conjugacion_esperada = self.conjugador_blob(verbo, pronombre)
        return respuesta_usuario.lower() == conjugacion_esperada

def main():
    # Verifica si se proporcionan suficientes argumentos
    if len(sys.argv) != 3:
        print("Uso: python test_conjugador.py <verbo> <pronombre>")
        return
    
    # Obtiene el verbo y el pronombre de los argumentos de la línea de comandos
    verbo = sys.argv[1]
    pronombre = sys.argv[2]

    # Crea una instancia de la clase ConjugadorFrances
    conjugador = ConjugadorFrances()

    # Conjugación esperada
    conjugacion_esperada = conjugador.conjugador_blob(verbo, pronombre)

    # Verificar la conjugación del verbo y pronombre
    conjugacion_correcta = conjugador.verificar_conjugacion(verbo, pronombre, conjugacion_esperada)

    # Mostrar el resultado
    if conjugacion_correcta:
        print(f"La conjugación para el verbo '{verbo}' y pronombre '{pronombre}' es correcta.")
    else:
        print(f"La conjugación para el verbo '{verbo}' y pronombre '{pronombre}' es incorrecta.")

if __name__ == "__main__":
    main()
