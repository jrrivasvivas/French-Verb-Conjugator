import csv
from datetime import datetime

class ErrorLogger:
    def __init__(self, log_filename):
        self.log_filename = f"{log_filename}_errors.csv"
        self._initialize_log_file()

    def _initialize_log_file(self):
        # Crea el archivo de registro si no existe
        with open(self.log_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            # Escribe el encabezado si el archivo está vacío
            if file.tell() == 0:
                writer.writerow(['Timestamp', 'User', 'Pronoun', 'Verb', 'Tense', 'User_Input', 'Correct_Conjugation', 'Result'])

    def log_error(self, user, pronoun, verb, tense, user_input, correct_conjugation, result):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_data = [timestamp, user, pronoun, verb, tense, user_input, correct_conjugation, result]

        with open(self.log_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(error_data)

    def read_log(self):
        # Lee el contenido del archivo de registro (si es necesario)
        with open(self.log_filename, 'r') as file:
            return file.read()

    def clear_log(self):
        # Borra el contenido del archivo de registro
        open(self.log_filename, 'w').close()
