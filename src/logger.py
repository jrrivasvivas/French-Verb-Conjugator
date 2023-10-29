import csv
import os
from datetime import datetime

class ErrorLogger:
    def __init__(self, month_year):
        self.month_year = month_year
        self.log_file = f"data/{month_year}.csv"  # Ruta para el archivo CSV en formato 'YYYYMM.csv'
        self._create_log_file()

    def _create_log_file(self):
        if not os.path.exists("data"):  # Utiliza la carpeta data/
            os.makedirs("data")

        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Fecha', 'Pronombre', 'Verbo', 'Tiempo Verbal', 'Conjugación Usuario', 'Conjugación Correcta', 'Resultado'])

    def log_error(self, pronoun, verb, tense, user_conjugation, correct_conjugation, result):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date_time, pronoun, verb, tense, user_conjugation, correct_conjugation, result])

# Uso del logger
# logger = ErrorLogger("202311")  # Crea el logger para el mes actual en un archivo 'YYYYMM.csv'
# logger.log_error(pronoun, verb, tense, user_conjugation, correct_conjugation, result)  # Registra un error en el CSV
