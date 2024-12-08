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
        'aller': {
            'subjonctif': {
                'je': 'aille',
                'tu': 'ailles',
                'il': 'aille',
                'nous': 'allions',
                'vous': 'alliez'
            }
        },
        'devoir': {
            'subjonctif': {
                'je': 'doive',
                'tu': 'doives',
                'il': 'doive',
                'nous': 'devions',
                'vous': 'deviez'
            }
        },
        'envoyer': {
            'subjonctif': {
                'je': 'envoie',
                'tu': 'envoies',
                'il': 'envoie',
                'nous': 'envoyions',
                'vous': 'envoyiez'
            }
        },
        'faire': {
            'subjonctif': {
                'je': 'fasse',
                'tu': 'fasses',
                'il': 'fasse',
                'nous': 'fassions',
                'vous': 'fassiez'
            }
        },
        'pouvoir': {
            'subjonctif': {
                'je': 'puisse',
                'tu': 'puisses',
                'il': 'puisse',
                'nous': 'puissions',
                'vous': 'puissiez'
            }
        },
        'recevoir': {
            'subjonctif': {
                'je': 'reçoive',
                'tu': 'reçoives',
                'il': 'reçoive',
                'nous': 'recevions',
                'vous': 'receviez'
            }
        },
        'savoir': {
            'subjonctif': {
                'je': 'sache',
                'tu': 'saches',
                'il': 'sache',
                'nous': 'sachions',
                'vous': 'sachiez'
            }
        },
        'venir': {
            'subjonctif': {
                'je': 'vienne',
                'tu': 'viennes',
                'il': 'vienne',
                'nous': 'venions',
                'vous': 'veniez'
            }
        },
        'voir': {
            'subjonctif': {
                'je': 'voie',
                'tu': 'voies',
                'il': 'voie',
                'nous': 'voyions',
                'vous': 'voyiez'
            }
        },
        'vouloir': {
            'subjonctif': {
                'je': 'veuille',
                'tu': 'veuilles',
                'il': 'veuille',
                'nous': 'voulions',
                'vous': 'vouliez'
            }
        },
        'adorer': {
            'subjonctif': {
                'je': 'adore',
                'tu': 'adores',
                'il': 'adore',
                'nous': 'adorions',
                'vous': 'adoriez'
            }
        },
        'regarder': {
            'subjonctif': {
                'je': 'regarde',
                'tu': 'regardes',
                'il': 'regarde',
                'nous': 'regardions',
                'vous': 'regardiez'
            }
        },
        'décider': {
            'subjonctif': {
                'je': 'décide',
                'tu': 'décides',
                'il': 'décide',
                'nous': 'décidions',
                'vous': 'décidiez'
            }
        },
        'prendre': {
            'subjonctif': {
                'je': 'prenne',
                'tu': 'prennes',
                'il': 'prenne',
                'nous': 'prenions',
                'vous': 'preniez'
            }
        },
        'arriver': {
            'subjonctif': {
                'je': 'arrive',
                'tu': 'arrives',
                'il': 'arrive',
                'nous': 'arrivions',
                'vous': 'arriviez'
            }
        },
        'neiger': {
            'subjonctif': {
                'il': 'neige'
            }
        },
        'attendre': {
            'subjonctif': {
                'je': 'attende',
                'tu': 'attendes',
                'il': 'attende',
                'nous': 'attendions',
                'vous': 'attendiez'
            }
        },
        'marcher': {
            'subjonctif': {
                'je': 'marche',
                'tu': 'marches',
                'il': 'marche',
                'nous': 'marchions',
                'vous': 'marchiez'
            }
        },
        'appeler': {
            'subjonctif': {
                'je': 'appelle',
                'tu': 'appelles',
                'il': 'appelle',
                'nous': 'appelions',
                'vous': 'appeliez'
            }
        },
        'revenir': {
            'subjonctif': {
                'je': 'revienne',
                'tu': 'reviennes',
                'il': 'revienne',
                'nous': 'revenions',
                'vous': 'reveniez'
            }
        },
        'se coucher': {
            'subjonctif': {
                'je': 'me couche',
                'tu': 'te couches',
                'il': 'se couche',
                'nous': 'nous couchions',
                'vous': 'vous couchiez'
            }
        },
        'entrer': {
            'subjonctif': {
                'je': 'entre',
                'tu': 'entres',
                'il': 'entre',
                'nous': 'entrions',
                'vous': 'entriez'
            }
        },
        'parler': {
            'subjonctif': {
                'je': 'parle',
                'tu': 'parles',
                'il': 'parle',
                'nous': 'parlions',
                'vous': 'parliez'
            }
        },
        'lire': {
            'subjonctif': {
                'je': 'lise',
                'tu': 'lises',
                'il': 'lise',
                'nous': 'lisions',
                'vous': 'lisiez'
            }
        },
        'partir': {
            'subjonctif': {
                'je': 'parte',
                'tu': 'partes',
                'il': 'parte',
                'nous': 'partions',
                'vous': 'partiez'
            }
        },
        'rencontrer': {
            'subjonctif': {
                'je': 'rencontre',
                'tu': 'rencontres',
                'il': 'rencontre',
                'nous': 'rencontrions',
                'vous': 'rencontriez'
            }
        },
        'jaser': {
            'subjonctif': {
                'je': 'jase',
                'tu': 'jases',
                'il': 'jase',
                'nous': 'jasions',
                'vous': 'jasiez'
            }
        },
        'passer': {
            'subjonctif': {
                'je': 'passe',
                'tu': 'passes',
                'il': 'passe',
                'nous': 'passions',
                'vous': 'passiez'
            }
        },
        'quitter': {
            'subjonctif': {
                'je': 'quitte',
                'tu': 'quittes',
                'il': 'quitte',
                'nous': 'quittions',
                'vous': 'quittiez'
            }
        },
        'répondre': {
            'subjonctif': {
                'je': 'réponde',
                'tu': 'répondes',
                'il': 'réponde',
                'nous': 'répondions',
                'vous': 'répondiez'
            }
        },
        'écrire': {
            'subjonctif': {
                'je': 'écrive',
                'tu': 'écrives',
                'il': 'écrive',
                'nous': 'écrivions',
                'vous': 'écriviez'
            }
        },
        's’améliorer': {
            'subjonctif': {
                'je': 'm’améliore',
                'tu': 't’améliore',
                'il': 's’améliore',
                'nous': 'nous améliorions',
                'vous': 'vous amélioriez'
            }
        },
        'se retrouver': {
            'subjonctif': {
                'je': 'me retrouve',
                'tu': 'te retrouves',
                'il': 'se retrouve',
                'nous': 'nous retrouvions',
                'vous': 'vous retrouviez'
            }
        },
        'trembler': {
            'subjonctif': {
                'je': 'tremble',
                'tu': 'trembles',
                'il': 'tremble',
                'nous': 'tremblions',
                'vous': 'trembliez'
            }
        },
        'réussir': {
            'subjonctif': {
                'je': 'réussisse',
                'tu': 'réussisses',
                'il': 'réussisse',
                'nous': 'réussissions',
                'vous': 'réussissiez'
            }
        },
        'se moquer': {
            'subjonctif': {
                'je': 'me moque',
                'tu': 'te moques',
                'il': 'se moque',
                'nous': 'nous moquions',
                'vous': 'vous moquiez'
            }
        },
        'se battre': {
            'subjonctif': {
                'je': 'me batte',
                'tu': 'te battes',
                'il': 'se batte',
                'nous': 'nous battions',
                'vous': 'vous battiez'
            }
        },
        'gagner': {
            'subjonctif': {
                'je': 'gagne',
                'tu': 'gagnes',
                'il': 'gagne',
                'nous': 'gagnions',
                'vous': 'gagniez'
            }
        },
        'picoter': {
            'subjonctif': {
                'je': 'picote',
                'tu': 'picotes',
                'il': 'picote',
                'nous': 'picotions',
                'vous': 'picotiez'
            }
        },
        'congestionner': {
            'subjonctif': {
                'je': 'congestionne',
                'tu': 'congestionnes',
                'il': 'congestionne',
                'nous': 'congestionnions',
                'vous': 'congestionniez'
            }
        },
        'sortir': {
            'subjonctif': {
                'je': 'sorte',
                'tu': 'sortes',
                'il': 'sorte',
                'nous': 'sortions',
                'vous': 'sortiez'
            }
        },
        'dormir': {
            'subjonctif': {
                'je': 'dorme',
                'tu': 'dormes',
                'il': 'dorme',
                'nous': 'dormions',
                'vous': 'dormiez'
            }
        },
                'aller': {
            'futur_simple': {
                'je': 'irai',
                'tu': 'iras',
                'il': 'ira',
                'nous': 'irons',
                'vous': 'irez'
            }
        },
        'avoir': {
            'futur_simple': {
                'je': 'aurai',
                'tu': 'auras',
                'il': 'aura',
                'nous': 'aurons',
                'vous': 'aurez'
            }
        },
        'devoir': {
            'futur_simple': {
                'je': 'devrai',
                'tu': 'devras',
                'il': 'devra',
                'nous': 'devrons',
                'vous': 'devrez'
            }
        },
        'envoyer': {
            'futur_simple': {
                'je': 'enverrai',
                'tu': 'enverras',
                'il': 'enverra',
                'nous': 'enverrons',
                'vous': 'enverrez'
            }
        },
        'être': {
            'futur_simple': {
                'je': 'serai',
                'tu': 'seras',
                'il': 'sera',
                'nous': 'serons',
                'vous': 'serez'
            }
        },
        'faire': {
            'futur_simple': {
                'je': 'ferai',
                'tu': 'feras',
                'il': 'fera',
                'nous': 'ferons',
                'vous': 'ferez'
            }
        },
        'pouvoir': {
            'futur_simple': {
                'je': 'pourrai',
                'tu': 'pourras',
                'il': 'pourra',
                'nous': 'pourrons',
                'vous': 'pourrez'
            }
        },
        'recevoir': {
            'futur_simple': {
                'je': 'recevrai',
                'tu': 'recevras',
                'il': 'recevra',
                'nous': 'recevrons',
                'vous': 'recevrez'
            }
        },
        'savoir': {
            'futur_simple': {
                'je': 'saurai',
                'tu': 'sauras',
                'il': 'saura',
                'nous': 'saurons',
                'vous': 'saurez'
            }
        },
        'venir': {
            'futur_simple': {
                'je': 'viendrai',
                'tu': 'viendras',
                'il': 'viendra',
                'nous': 'viendrons',
                'vous': 'viendrez'
            }
        },
        'voir': {
            'futur_simple': {
                'je': 'verrai',
                'tu': 'verras',
                'il': 'verra',
                'nous': 'verrons',
                'vous': 'verrez'
            }
        },
        'vouloir': {
            'futur_simple': {
                'je': 'voudrai',
                'tu': 'voudras',
                'il': 'voudra',
                'nous': 'voudrons',
                'vous': 'voudrez'
            }
        },
                'aller': {
            'imparfait': {
                'je': 'allais',
                'tu': 'allais',
                'il': 'allait',
                'nous': 'allions',
                'vous': 'alliez'
            }
        },
        'avoir': {
            'imparfait': {
                'je': 'avais',
                'tu': 'avais',
                'il': 'avait',
                'nous': 'avions',
                'vous': 'aviez'
            }
        },
        'devoir': {
            'imparfait': {
                'je': 'devais',
                'tu': 'devais',
                'il': 'devait',
                'nous': 'devions',
                'vous': 'deviez'
            }
        },
        'envoyer': {
            'imparfait': {
                'je': 'envoyais',
                'tu': 'envoyais',
                'il': 'envoyait',
                'nous': 'envoyions',
                'vous': 'envoyiez'
            }
        },
        'être': {
            'imparfait': {
                'je': 'étais',
                'tu': 'étais',
                'il': 'était',
                'nous': 'étions',
                'vous': 'étiez'
            }
        },
        'faire': {
            'imparfait': {
                'je': 'faisais',
                'tu': 'faisais',
                'il': 'faisait',
                'nous': 'faisions',
                'vous': 'faisiez'
            }
        },
        'pouvoir': {
            'imparfait': {
                'je': 'pouvais',
                'tu': 'pouvais',
                'il': 'pouvait',
                'nous': 'pouvions',
                'vous': 'pouviez'
            }
        },
        'recevoir': {
            'imparfait': {
                'je': 'recevais',
                'tu': 'recevais',
                'il': 'recevait',
                'nous': 'recevions',
                'vous': 'receviez'
            }
        },
        'savoir': {
            'imparfait': {
                'je': 'savais',
                'tu': 'savais',
                'il': 'savait',
                'nous': 'savions',
                'vous': 'saviez'
            }
        },
        'venir': {
            'imparfait': {
                'je': 'venais',
                'tu': 'venais',
                'il': 'venait',
                'nous': 'venions',
                'vous': 'veniez'
            }
        },
        'voir': {
            'imparfait': {
                'je': 'voyais',
                'tu': 'voyais',
                'il': 'voyait',
                'nous': 'voyions',
                'vous': 'voyiez'
            }
        },
        'vouloir': {
            'imparfait': {
                'je': 'voulais',
                'tu': 'voulais',
                'il': 'voulait',
                'nous': 'voulions',
                'vous': 'vouliez'
            }
        },
        'adorer': {
            'imparfait': {
                'je': 'adorais',
                'tu': 'adorais',
                'il': 'adorait',
                'nous': 'adorions',
                'vous': 'adoriez'
            }
        },
        'regarder': {
            'imparfait': {
                'je': 'regardais',
                'tu': 'regardais',
                'il': 'regardait',
                'nous': 'regardions',
                'vous': 'regardiez'
            }
        },
        'décider': {
            'imparfait': {
                'je': 'décidais',
                'tu': 'décidais',
                'il': 'décidait',
                'nous': 'décidions',
                'vous': 'décidiez'
            }
        },
        'prendre': {
            'imparfait': {
                'je': 'prenais',
                'tu': 'prenais',
                'il': 'prenait',
                'nous': 'prenions',
                'vous': 'preniez'
            }
        },
        'arriver': {
            'imparfait': {
                'je': 'arrivais',
                'tu': 'arrivais',
                'il': 'arrivait',
                'nous': 'arrivions',
                'vous': 'arriviez'
            }
        },
        'neiger': {
            'imparfait': {
                'il': 'neigeait'
            }
        },
        'attendre': {
            'imparfait': {
                'je': 'attendais',
                'tu': 'attendais',
                'il': 'attendait',
                'nous': 'attendions',
                'vous': 'attendiez'
            }
        },
        'marcher': {
            'imparfait': {
                'je': 'marchais',
                'tu': 'marchais',
                'il': 'marchait',
                'nous': 'marchions',
                'vous': 'marchiez'
            }
        },
        'appeler': {
            'imparfait': {
                'je': 'appelais',
                'tu': 'appelais',
                'il': 'appelait',
                'nous': 'appelions',
                'vous': 'appeliez'
            }
        },
        'revenir': {
            'imparfait': {
                'je': 'revenais',
                'tu': 'revenais',
                'il': 'revenait',
                'nous': 'revenions',
                'vous': 'reveniez'
            }
        },
        'se coucher': {
            'imparfait': {
                'je': 'me couchais',
                'tu': 'te couchais',
                'il': 'se couchait',
                'nous': 'nous couchions',
                'vous': 'vous couchiez'
            }
        },
        'entrer': {
            'imparfait': {
                'je': 'entrais',
                'tu': 'entrais',
                'il': 'entrait',
                'nous': 'entrions',
                'vous': 'entriez'
            }
        },
        'parler': {
            'imparfait': {
                'je': 'parlais',
                'tu': 'parlais',
                'il': 'parlait',
                'nous': 'parlions',
                'vous': 'parliez'
            }
        },
        'lire': {
            'imparfait': {
                'je': 'lisais',
                'tu': 'lisais',
                'il': 'lisait',
                'nous': 'lisions',
                'vous': 'lisiez'
            }
        },
        'partir': {
            'imparfait': {
                'je': 'partais',
                'tu': 'partais',
                'il': 'partait',
                'nous': 'partions',
                'vous': 'partiez'
            }
        },
        'rencontrer': {
            'imparfait': {
                'je': 'rencontrais',
                'tu': 'rencontrais',
                'il': 'rencontrait',
                'nous': 'rencontrions',
                'vous': 'rencontriez'
            }
        },
        'jaser': {
            'imparfait': {
                'je': 'jasais',
                'tu': 'jasais',
                'il': 'jasait',
                'nous': 'jasions',
                'vous': 'jasiez'
            }
        },
        'passer': {
            'imparfait': {
                'je': 'passais',
                'tu': 'passais',
                'il': 'passait',
                'nous': 'passions',
                'vous': 'passiez'
            }
        },
        'quitter': {
            'imparfait': {
                'je': 'quittais',
                'tu': 'quittais',
                'il': 'quittait',
                'nous': 'quittions',
                'vous': 'quittiez'
            }
        },
        'répondre': {
            'imparfait': {
                'je': 'répondais',
                'tu': 'répondais',
                'il': 'répondait',
                'nous': 'répondions',
                'vous': 'répondiez'
            }
        },
        'écrire': {
            'imparfait': {
                'je': 'écrivais',
                'tu': 'écrivais',
                'il': 'écrivait',
                'nous': 'écrivions',
                'vous': 'écriviez'
            }
        },
        's’améliorer': {
            'imparfait': {
                'je': 'm’améliorais',
                'tu': 't’améliorais',
                'il': 's’améliorait',
                'nous': 'nous améliorions',
                'vous': 'vous amélioriez'
            }
        },
        's’améliorer': {
            'imparfait': {
                'je': 'm’améliorais',
                'tu': 't’améliorais',
                'il': 's’améliorait',
                'nous': 'nous améliorions',
                'vous': 'vous amélioriez'
            }
        },
        'se retrouver': {
            'imparfait': {
                'je': 'me retrouvais',
                'tu': 'te retrouvais',
                'il': 'se retrouvait',
                'nous': 'nous retrouvions',
                'vous': 'vous retrouviez'
            }
        },
        'trembler': {
            'imparfait': {
                'je': 'tremblais',
                'tu': 'tremblais',
                'il': 'tremblait',
                'nous': 'tremblions',
                'vous': 'trembliez'
            }
        },
        'réussir': {
            'imparfait': {
                'je': 'réussissais',
                'tu': 'réussissais',
                'il': 'réussissait',
                'nous': 'réussissions',
                'vous': 'réussissiez'
            }
        },
        'se moquer': {
            'imparfait': {
                'je': 'me moquais',
                'tu': 'te moquais',
                'il': 'se moquait',
                'nous': 'nous moquions',
                'vous': 'vous moquiez'
            }
        },
        'se battre': {
            'imparfait': {
                'je': 'me battais',
                'tu': 'te battais',
                'il': 'se battait',
                'nous': 'nous battions',
                'vous': 'vous battiez'
            }
        },
        'gagner': {
            'imparfait': {
                'je': 'gagnais',
                'tu': 'gagnais',
                'il': 'gagnait',
                'nous': 'gagnions',
                'vous': 'gagniez'
            }
        },
        'picoter': {
            'imparfait': {
                'je': 'picotais',
                'tu': 'picotais',
                'il': 'picotait',
                'nous': 'picotions',
                'vous': 'picotiez'
            }
        },
        'congestionner': {
            'imparfait': {
                'je': 'congestionnais',
                'tu': 'congestionnais',
                'il': 'congestionnait',
                'nous': 'congestionnions',
                'vous': 'congestionniez'
            }
        },
        'sortir': {
            'imparfait': {
                'je': 'sortais',
                'tu': 'sortais',
                'il': 'sortait',
                'nous': 'sortions',
                'vous': 'sortiez'
            }
        },
        'dormir': {
            'imparfait': {
                'je': 'dormais',
                'tu': 'dormais',
                'il': 'dormait',
                'nous': 'dormions',
                'vous': 'dormiez'
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