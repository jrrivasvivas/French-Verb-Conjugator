import random
from .verbs import Conjugator
from .player import Player
from .logger import ErrorLogger

class ConjugationGameLogic:
    def __init__(self, players, error_logger):
        self.conjugator = Conjugator()
        self.players = {player.name: player for player in players}
        self.error_logger = error_logger

    def play_round(self, player_name, user_input):
        player = self.players.get(player_name)
        if player:
            verb, pronoun, tense = self.conjugator.generate_random_verb()
            correct_conjugation = self.conjugator.conjugate(verb, pronoun, tense)
            
            user_verb = user_input.split(' ', 1)[-1]
            correct = user_verb == correct_conjugation and user_input.startswith(pronoun)
            player.update_score(correct)

            result = 'Correct' if correct else f"Incorrect. La conjugaison correcte est : {pronoun} {correct_conjugation}"
            self.error_logger.log_error(player_name, pronoun, verb, tense, user_verb, correct_conjugation, result)

            return {
                'verb': verb,
                'pronoun': pronoun,
                'tense': tense,
                'result': result
            }
        else:
            raise ValueError("Jugador no encontrado.")
    
    def get_total_score(self, player_name):
        player = self.players.get(player_name)
        if player:
            return player.get_total_score()
        else:
            raise ValueError("Jugador no encontrado.")
