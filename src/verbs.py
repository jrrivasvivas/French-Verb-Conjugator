import random

class Conjugator:
    verb_dict = {
        'etre': {
            'present': {
                'je': 'suis',
                'tu': 'es',
                'il': 'est',
                'nous': 'sommes',
                'vous': 'êtes'
            }
        },
        'avoir': {
            'present': {
                'je': 'ai',
                'tu': 'as',
                'il': 'a',
                'nous': 'avons',
                'vous': 'avez'
            }
        },
        'aller': {
            'present': {
                'je': 'vais',
                'tu': 'vas',
                'il': 'va',
                'nous': 'allons',
                'vous': 'allez'
            }
        }
    }

    @staticmethod
    def conjugate(verb, pronoun, tense):
        try:
            return Conjugator.verb_dict[verb][tense][pronoun]
        except KeyError:
            return None
    
    @staticmethod
    def generate_random_verb():
        verb = random.choice(list(Conjugator.verb_dict.keys()))
        tense = random.choice(list(Conjugator.verb_dict[verb].keys()))
        pronoun = random.choice(list(Conjugator.verb_dict[verb][tense].keys()))
        return verb, pronoun, tense
