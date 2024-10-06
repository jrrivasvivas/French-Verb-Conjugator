from src.verbs import Conjugator  # Importar Conjugator desde verbs.py en la carpeta src
from src.logger import ErrorLogger  # Importar ErrorLogger desde logger.py en la carpeta src

from blessed import Terminal
from src.verbs import Conjugator  # Importar Conjugator desde verbs.py en la carpeta src
from src.logger import ErrorLogger  # Importar ErrorLogger desde logger.py en la carpeta src

class ConjugationGame:
    def __init__(self):
        # Inicializar Conjugator y ErrorLogger
        self.conjugator = Conjugator()
        self.logger = ErrorLogger("2023-11")  # Crear un ErrorLogger para el mes actual
        self.score = {'correct': 0, 'incorrect': 0}
        self.tenses_selected = []  # Aquí se almacenan los tiempos verbales seleccionados
        self.term = Terminal()  # Crear un objeto terminal

        # Pedir nombre del jugador
        while True:
            first_name = input("Entrez votre prénom : ")
            if ' ' not in first_name:
                self.user_name = first_name.lower()
                break
            else:
                print("Veuillez entrer seulement votre prénom.")

    def menu_selection_temps(self):
        # Opciones del menú
        tenses = ['Présent', 'Passé', 'Futur_simple', 'Subjonctif', 'Imparfait']
        selected = [False] * len(tenses)

        # Inicializamos el terminal
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            print(self.term.clear())
            print(self.term.move(0, 0) + "Sélectionnez les temps verbaux avec la barre d'espace et appuyez sur 'Enter' pour valider :\n")
            
            current_row = 0

            while True:
                # Limpiar la pantalla para evitar duplicaciones
                print(self.term.clear())

                # Mostrar el mensaje de selección
                print(self.term.move(0, 0) + "Sélectionnez les temps verbaux avec la barre d'espace et appuyez sur 'Enter' pour valider :\n")

                # Mostrar las opciones del menú con sus estados de selección
                for idx, tense in enumerate(tenses):
                    if idx == current_row:
                        if selected[idx]:
                            print(self.term.reverse("[X] " + tense))
                        else:
                            print(self.term.reverse("[ ] " + tense))
                    else:
                        if selected[idx]:
                            print("[X] " + tense)
                        else:
                            print("[ ] " + tense)

                key = self.term.inkey()

                if key.code in (self.term.KEY_UP, 'k'):  # Mover hacia arriba
                    current_row = (current_row - 1) % len(tenses)
                elif key.code in (self.term.KEY_DOWN, 'j'):  # Mover hacia abajo
                    current_row = (current_row + 1) % len(tenses)
                elif key == ' ':  # Seleccionar/deseleccionar con la barra espaciadora
                    selected[current_row] = not selected[current_row]
                elif key.code in (self.term.KEY_ENTER, '\n', '\r'):  # Enter para confirmar
                    break

        # Guardar los tiempos verbales seleccionados
        self.tenses_selected = [tense.lower() for idx, tense in enumerate(tenses) if selected[idx]]
        if not self.tenses_selected:
            print("Aucun temps verbal sélectionné, vous allez pratiquer le 'Présent'.")
            self.tenses_selected = ['present']  # Si no selecciona nada, por defecto será el presente

    def play_round(self):
        # Generar un verbo aleatorio de los tiempos seleccionados
        verb, pronoun, tense = self.conjugator.generate_random_verb(self.tenses_selected)
        print(f"Conjuguez le verbe '{verb}' à '{pronoun}' au '{tense}'.")

        user_input = input("Entrez la conjugaison (pronom verbe) : ")

        # Separar el input en palabras
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

    def start_game(self):
        print("Bienvenue au jeu de conjugaison des verbes !")

        # Mostrar el menú para seleccionar los tiempos verbales
        self.menu_selection_temps()

        while True:
            self.play_round()
            print(f"Réussites : {self.score['correct']} - Erreurs : {self.score['incorrect']}")
            play_again = input("Voulez-vous jouer à nouveau ? (o/n) : ").lower()
            if play_again != 'o':
                print("Merci d'avoir joué ! Au revoir.")
                break