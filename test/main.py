from verbs import Conjugator

class ConjugationGame:
    def __init__(self):
        self.conjugator = Conjugator()
        self.score = {'correct': 0, 'incorrect': 0}

    def play_round(self):
        verb, pronoun, tense = self.conjugator.generate_random_verb()

        print(f"Conjugue el verbo '{verb}' en '{pronoun}' en '{tense}'.")

        user_input = input("Ingrese la conjugación (pronombre verbo): ")
        user_pronoun, user_verb = user_input.split()

        correct_conjugation = self.conjugator.conjugate(verb, pronoun, tense)

        if user_verb == correct_conjugation and user_pronoun == pronoun:
            print("¡Correcto!")
            self.score['correct'] += 1
        else:
            print(f"Incorrecto. La conjugación correcta es: {pronoun} {correct_conjugation}")
            self.score['incorrect'] += 1

    def start_game(self):
        print("¡Bienvenido al juego de conjugación de verbos!")
        while True:
            self.play_round()
            print(f"Aciertos: {self.score['correct']} - Errores: {self.score['incorrect']}")
            play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if play_again != 's':
                print("¡Gracias por jugar! Hasta luego.")
                break

if __name__ == "__main__":
    game = ConjugationGame()
    game.start_game()
