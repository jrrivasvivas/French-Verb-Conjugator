class Player:
    def __init__(self, name):
        self.name = name
        self.score_history = {'correct': 0, 'incorrect': 0}

    def update_score(self, correct):
        if correct:
            self.score_history['correct'] += 1
        else:
            self.score_history['incorrect'] += 1

    def get_total_score(self):
        return f"Réussites : {self.score_history['correct']} - Erreurs : {self.score_history['incorrect']}"
