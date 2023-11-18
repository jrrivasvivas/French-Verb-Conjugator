from src.verbs import Conjugator
from src.logger import ErrorLogger

class ConjugationGame:
    def __init__(self, user_name=None):
        self.conjugator = Conjugator()
        self.logger = ErrorLogger("2023-11")
        self.score = {'correct': 0, 'incorrect': 0}
        self.user_name = user_name

        if self.user_name is None:
            self._get_user_name()

    def _get_user_name(self):
        # No se requiere la entrada de usuario aquí, ya que se obtiene desde la interfaz web en la aplicación Dash
        pass

    def play_round(self, user_input=None):
        verb, pronoun, tense = self.conjugator.generate_random_verb()

        if user_input is None:
            # La entrada de usuario no se proporciona, asumimos el modo de consola
            print(f"Conjuguez le verbe '{verb}' à '{pronoun}' au '{tense}'.")
            user_input = input("Entrez la conjugaison (pronom verbe) : ")

        words = user_input.split()

        if len(words) >= 2:
            user_pronoun = words[0]
            user_verb = ' '.join(words[1:])
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

        self.logger.log_error(self.user_name, pronoun, verb, tense, user_verb, correct_conjugation, result)

    def get_score(self):
        return f"Réussites : {self.score['correct']} - Erreurs : {self.score['incorrect']}"