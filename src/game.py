from src.verbs import Conjugator  # Importar Conjugator desde verbs.py en la carpeta src
from src.logger import ErrorLogger  # Importar ErrorLogger desde logger.py en la carpeta src

class ConjugationGame:
    def __init__(self):
        # Initialize Conjugator and ErrorLogger objects
        self.conjugator = Conjugator()
        self.logger = ErrorLogger("2023-11")  # Create an ErrorLogger object for the current month
        self.score = {'correct': 0, 'incorrect': 0}

    def play_round(self):
        # Generate a random verb and prompt user input
        verb, pronoun, tense = self.conjugator.generate_random_verb()
        print(f"Conjuguez le verbe '{verb}' à '{pronoun}' au '{tense}'.")

        user_input = input("Entrez la conjugaison (pronom verbe) : ")

        # Split the input into words
        words = user_input.split()

        # Verify if there are enough words (at least two) in the input
        if len(words) >= 2:
            user_pronoun = words[0]  # The first word is the pronoun
            user_verb = ' '.join(words[1:])  # The rest of the words are the verb (even if it contains spaces)
        else:
            print("Entrée invalide. Doit inclure au moins un pronom et un verbe.")
            return

        correct_conjugation = self.conjugator.conjugate(verb, pronoun, tense)

        if user_verb == correct_conjugation and user_pronoun == pronoun:
            print("Correct !")
            self.score['correct'] += 1
            result = 'Correct'
        else:
            print(f"Incorrect. La conjugaison correcte est : {pronoun} {correct_conjugation}")
            self.score['incorrect'] += 1
            result = 'Incorrect'

        self.logger.log_error(pronoun, verb, tense, user_verb, correct_conjugation, result)

    def start_game(self):
        print("Bienvenue au jeu de conjugaison des verbes !")
        while True:
            self.play_round()
            print(f"Réussites : {self.score['correct']} - Erreurs : {self.score['incorrect']}")
            play_again = input("Voulez-vous jouer à nouveau ? (o/n) : ").lower()
            if play_again != 'o':
                print("Merci d'avoir joué ! Au revoir.")
                break
