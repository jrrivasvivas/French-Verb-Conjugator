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
    },
    'chanter': {
        'present': {
            'je': 'chante',
            'tu': 'chantes',
            'il': 'chante',
            'nous': 'chantons',
            'vous': 'chantez'
        }
    },
    "s'appeler": {
        'present': {
            'je': "m'appelle",
            'tu': "t'appelles",
            'il': "s'appelle",
            'nous': "nous appelons",
            'vous': "vous appelez"
        }
    },
    'finir': {
        'present': {
            'je': 'finis',
            'tu': 'finis',
            'il': 'finit',
            'nous': 'finissons',
            'vous': 'finissez'
        }
    },
    'conduire': {
        'present': {
            'je': 'conduis',
            'tu': 'conduis',
            'il': 'conduit',
            'nous': 'conduisons',
            'vous': 'conduisez'
        }
    },
    'dire': {
        'present': {
            'je': 'dis',
            'tu': 'dis',
            'il': 'dit',
            'nous': 'disons',
            'vous': 'dites'
        }
    },
    'voir': {
        'present': {
            'je': 'vois',
            'tu': 'vois',
            'il': 'voit',
            'nous': 'voyons',
            'vous': 'voyez'
        }
    },
    'boire': {
        'present': {
            'je': 'bois',
            'tu': 'bois',
            'il': 'boit',
            'nous': 'buvons',
            'vous': 'buvez'
        }
    },
    'venir': {
        'present': {
            'je': 'viens',
            'tu': 'viens',
            'il': 'vient',
            'nous': 'venons',
            'vous': 'venez'
        }
    },
    'croire': {
        'present': {
            'je': 'crois',
            'tu': 'crois',
            'il': 'croit',
            'nous': 'croyons',
            'vous': 'croyez'
        }
    },
    'produire': {
        'present': {
            'je': 'produis',
            'tu': 'produis',
            'il': 'produit',
            'nous': 'produisons',
            'vous': 'produisez'
        }
    },
    'faire': {
        'present': {
            'je': 'fais',
            'tu': 'fais',
            'il': 'fait',
            'nous': 'faisons',
            'vous': 'faites'
        }
    },
    'courir': {
        'present': {
            'je': 'cours',
            'tu': 'cours',
            'il': 'court',
            'nous': 'courons',
            'vous': 'courez'
        }
    },
    'savoir': {
        'present': {
            'je': 'sais',
            'tu': 'sais',
            'il': 'sait',
            'nous': 'savons',
            'vous': 'savez'
        }
    },
    'connaitre': {
        'present': {
            'je': 'connais',
            'tu': 'connais',
            'il': 'connait',
            'nous': 'connaissons',
            'vous': 'connaissez'
        }
    },
    'devoir': {
        'present': {
            'je': 'dois',
            'tu': 'dois',
            'il': 'doit',
            'nous': 'devons',
            'vous': 'devez'
        }
    },
    'vouloir': {
        'present': {
            'je': 'veux',
            'tu': 'veux',
            'il': 'veut',
            'nous': 'voulons',
            'vous': 'voulez'
        }
    },
    'pouvoir': {
        'present': {
            'je': 'peux',
            'tu': 'peux',
            'il': 'peut',
            'nous': 'pouvons',
            'vous': 'pouvez'
        }
    },
    'dormir': {
        'present': {
            'je': 'dors',
            'tu': 'dors',
            'il': 'dort',
            'nous': 'dormons',
            'vous': 'dormez'
        }
    },
    'ecrire': {
        'present': {
            'je': 'écris',
            'tu': 'écris',
            'il': 'écrit',
            'nous': 'écrivons',
            'vous': 'écrivez'
        }
    },
    'lire': {
        'present': {
            'je': 'lis',
            'tu': 'lis',
            'il': 'lit',
            'nous': 'lisons',
            'vous': 'lisez'
        }
    },
    'suivre': {
        'present': {
            'je': 'suis',
            'tu': 'suis',
            'il': 'suit',
            'nous': 'suivons',
            'vous': 'suivez'
        }
    },
    'prendre': {
        'present': {
            'je': 'prends',
            'tu': 'prends',
            'il': 'prend',
            'nous': 'prenons',
            'vous': 'prenez'
        }
    },
    'attendre': {
        'present': {
            'je': 'attends',
            'tu': 'attends',
            'il': 'attend',
            'nous': 'attendons',
            'vous': 'attendez'
        }
    },
    'mettre': {
        'present': {
            'je': 'mets',
            'tu': 'mets',
            'il': 'met',
            'nous': 'mettons',
            'vous': 'mettez'
        }
    },
    'recevoir': {
        'present': {
            'je': 'reçois',
            'tu': 'reçois',
            'il': 'reçoit',
            'nous': 'recevons',
            'vous': 'recevez'
        }
    },
    'offrir': {
        'present': {
            'je': 'offre',
            'tu': 'offres',
            'il': 'offre',
            'nous': 'offrons',
            'vous': 'offrez'
        }
    },
    'decouvrir': {
        'present': {
            'je': 'découvre',
            'tu': 'découvres',
            'il': 'découvre',
            'nous': 'découvrons',
            'vous': 'découvrez'
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
