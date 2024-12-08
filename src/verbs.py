import random

class Conjugator:
    
    verb_dict = {
    "etre": {
        "present": {
            "je": "suis",
            "tu": "es",
            "il": "est",
            "nous": "sommes",
            "vous": "êtes"
        },
        "passe_composse": {
            "je": "j'ai été",
            "tu": "as été",
            "il": "a été",
            "nous": "avons été",
            "vous": "avez été"
        },
        "futur_simple": {
            "je": "serai",
            "tu": "seras",
            "il": "sera",
            "nous": "serons",
            "vous": "serez"
        },
        "imparfait": {
            "je": "étais",
            "tu": "étais",
            "il": "était",
            "nous": "étions",
            "vous": "étiez"
        },
        "subjonctif": {
            "que je": "sois",
            "que tu": "sois",
            "qu'il": "soit",
            "que nous": "soyons",
            "que vous": "soyez"
        },
        "conditionnel_present": {
            "je": "serais",
            "tu": "serais",
            "il": "serait",
            "nous": "serions",
            "vous": "seriez"
        }
    },
    "avoir": {
        "present": {
            "je": "j'ai",
            "tu": "as",
            "il": "a",
            "nous": "avons",
            "vous": "avez"
        },
        "passe_composse": {
            "je": "j'ai eu",
            "tu": "as eu",
            "il": "a eu",
            "nous": "avons eu",
            "vous": "avez eu"
        },
        "futur_simple": {
            "je": "aurai",
            "tu": "auras",
            "il": "aura",
            "nous": "aurons",
            "vous": "aurez"
        },
        "imparfait": {
            "je": "avais",
            "tu": "avais",
            "il": "avait",
            "nous": "avions",
            "vous": "aviez"
        },
        "subjonctif": {
            "que je": "aie",
            "que tu": "aies",
            "qu'il": "ait",
            "que nous": "ayons",
            "que vous": "ayez"
        },
        "conditionnel_present": {
            "je": "aurais",
            "tu": "aurais",
            "il": "aurait",
            "nous": "aurions",
            "vous": "auriez"
        }
    },
    "aller": {
        "present": {
            "je": "vais",
            "tu": "vas",
            "il": "va",
            "nous": "allons",
            "vous": "allez"
        },
        "passe_composse": {
            "je": "suis allé",
            "tu": "es allé",
            "il": "est allé",
            "nous": "sommes allés",
            "vous": "êtes allés"
        },
        "futur_simple": {
            "je": "irai",
            "tu": "iras",
            "il": "ira",
            "nous": "irons",
            "vous": "irez"
        },
        "imparfait": {
            "je": "allais",
            "tu": "allais",
            "il": "allait",
            "nous": "allions",
            "vous": "alliez"
        },
        "subjonctif": {
            "que je": "aille",
            "que tu": "ailles",
            "qu'il": "aille",
            "que nous": "allions",
            "que vous": "alliez"
        },
        "conditionnel_present": {
            "je": "irais",
            "tu": "irais",
            "il": "irait",
            "nous": "irions",
            "vous": "iriez"
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
    def generate_random_verb(selected_tenses):
        # Filtrar los verbos que tienen los tiempos seleccionados
        verbs_with_selected_tenses = {
            verb: {tense: conjugations for tense, conjugations in tenses.items() if tense in selected_tenses}
            for verb, tenses in Conjugator.verb_dict.items()
            if any(tense in selected_tenses for tense in tenses.keys())
        }

        # Asegurarse de que haya verbos con tiempos seleccionados
        if not verbs_with_selected_tenses:
            raise ValueError("No hay verbos disponibles con los tiempos seleccionados.")

        # Elegir un verbo al azar que tenga tiempos seleccionados
        verb = random.choice(list(verbs_with_selected_tenses.keys()))

        # Elegir un tiempo que esté entre los seleccionados
        tense = random.choice(list(verbs_with_selected_tenses[verb].keys()))

        # Elegir un pronombre al azar
        pronoun = random.choice(list(verbs_with_selected_tenses[verb][tense].keys()))

        return verb, pronoun, tense
