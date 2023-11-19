import random

class Conjugator:
    verb_dict = {
    'etre': {
        'present': {
            'je': 'suis',
            'tu': 'es',
            'il': 'est',
            'elle': 'est',
            'nous': 'sommes',
            'vous': 'êtes',
            'ils': 'sont',
            'elles': 'sont'
        },
        'passe_compose': {
            'je': 'ai été',
            'tu': 'as été',
            'il': 'a été',
            'elle': 'a été',
            'nous': 'avons été',
            'vous': 'avez été',
            'ils': 'ont été',
            'elles': 'ont été'
        }
    },
    'avoir': {
        'present': {
            'je': 'ai',
            'tu': 'as',
            'il': 'a',
            'elle': 'a',
            'nous': 'avons',
            'vous': 'avez',
            'ils': 'ont',
            'elles': 'ont'
        },
        'passe_compose': {
            'je': 'ai eu',
            'tu': 'as eu',
            'il': 'a eu',
            'elle': 'a eu',
            'nous': 'avons eu',
            'vous': 'avez eu',
            'ils': 'ont eu',
            'elles': 'ont eu'
        }
    },
    'aller': {
        'present': {
            'je': 'vais',
            'tu': 'vas',
            'il': 'va',
            'elle': 'va',
            'nous': 'allons',
            'vous': 'allez',
            'ils': 'vont',
            'elles': 'vont'
        },
        'passe_compose': {
            'je': 'suis allé',
            'tu': 'es allé',
            'il': 'est allé',
            'elle': 'est allée',
            'nous': 'sommes allés',
            'vous': 'êtes allés',
            'ils': 'sont allés',
            'elles': 'sont allées'
        }
    },
    'chanter': {
        'present': {
            'je': 'chante',
            'tu': 'chantes',
            'il': 'chante',
            'elle': 'chante',
            'nous': 'chantons',
            'vous': 'chantez',
            'ils': 'chantent',
            'elles': 'chantent'
        },
        'passe_compose': {
            'je': 'ai chanté',
            'tu': 'as chanté',
            'il': 'a chanté',
            'elle': 'a chanté',
            'nous': 'avons chanté',
            'vous': 'avez chanté',
            'ils': 'ont chanté',
            'elles': 'ont chanté'
        }
    },
    "s'appeler": {
        'present': {
            'je': "m'appelle",
            'tu': "t'appelles",
            'il': "s'appelle",
            'elle': "s'appelle",
            'nous': "nous appelons",
            'vous': "vous appelez",
            'ils': "s'appellent",
            'elles': "s'appellent"
        },
        'passe_compose': {
            'je': "me suis appelé",
            'tu': "t'es appelé",
            'il': "s'est appelé",
            'elle': "s'est appelée",
            'nous': "nous sommes appelés",
            'vous': "vous êtes appelés",
            'ils': "se sont appelés",
            'elles': "se sont appelées"
        }
    },
    'finir': {
        'present': {
            'je': 'finis',
            'tu': 'finis',
            'il': 'finit',
            'elle': 'finit',
            'nous': 'finissons',
            'vous': 'finissez',
            'ils': 'finissent',
            'elles': 'finissent'
        },
        'passe_compose': {
            'je': 'ai fini',
            'tu': 'as fini',
            'il': 'a fini',
            'elle': 'a fini',
            'nous': 'avons fini',
            'vous': 'avez fini',
            'ils': 'ont fini',
            'elles': 'ont fini'
        }
    },
    'conduire': {
        'present': {
            'je': 'conduis',
            'tu': 'conduis',
            'il': 'conduit',
            'elle': 'conduit',
            'nous': 'conduisons',
            'vous': 'conduisez',
            'ils': 'conduisent',
            'elles': 'conduisent'
        },
        'passe_compose': {
            'je': 'ai conduit',
            'tu': 'as conduit',
            'il': 'a conduit',
            'elle': 'a conduit',
            'nous': 'avons conduit',
            'vous': 'avez conduit',
            'ils': 'ont conduit',
            'elles': 'ont conduit'
        }
    },
    'dire': {
        'present': {
            'je': 'dis',
            'tu': 'dis',
            'il': 'dit',
            'elle': 'dit',
            'nous': 'disons',
            'vous': 'dites',
            'ils': 'disent',
            'elles': 'disent'
        },
        'passe_compose': {
            'je': 'ai dit',
            'tu': 'as dit',
            'il': 'a dit',
            'elle': 'a dit',
            'nous': 'avons dit',
            'vous': 'avez dit',
            'ils': 'ont dit',
            'elles': 'ont dit'
        }
    },
    'voir': {
        'present': {
            'je': 'vois',
            'tu': 'vois',
            'il': 'voit',
            'elle': 'voit',
            'nous': 'voyons',
            'vous': 'voyez',
            'ils': 'voient',
            'elles': 'voient'
        },
        'passe_compose': {
            'je': 'ai vu',
            'tu': 'as vu',
            'il': 'a vu',
            'elle': 'a vu',
            'nous': 'avons vu',
            'vous': 'avez vu',
            'ils': 'ont vu',
            'elles': 'ont vu'
        }
    },
    'boire': {
        'present': {
            'je': 'bois',
            'tu': 'bois',
            'il': 'boit',
            'elle': 'boit',
            'nous': 'buvons',
            'vous': 'buvez',
            'ils': 'boivent',
            'elles': 'boivent'
        },
        'passe_compose': {
            'je': 'ai bu',
            'tu': 'as bu',
            'il': 'a bu',
            'elle': 'a bu',
            'nous': 'avons bu',
            'vous': 'avez bu',
            'ils': 'ont bu',
            'elles': 'ont bu'
        }
    },
    'voir': {
        'present': {
            'je': 'vois',
            'tu': 'vois',
            'il': 'voit',
            'elle': 'voit',
            'nous': 'voyons',
            'vous': 'voyez',
            'ils': 'voient',
            'elles': 'voient'
        },
        'passe_compose': {
            'je': 'ai vu',
            'tu': 'as vu',
            'il': 'a vu',
            'elle': 'a vu',
            'nous': 'avons vu',
            'vous': 'avez vu',
            'ils': 'ont vu',
            'elles': 'ont vu'
        }
    },
    'boire': {
        'present': {
            'je': 'bois',
            'tu': 'bois',
            'il': 'boit',
            'elle': 'boit',
            'nous': 'buvons',
            'vous': 'buvez',
            'ils': 'boivent',
            'elles': 'boivent'
        },
        'passe_compose': {
            'je': 'ai bu',
            'tu': 'as bu',
            'il': 'a bu',
            'elle': 'a bu',
            'nous': 'avons bu',
            'vous': 'avez bu',
            'ils': 'ont bu',
            'elles': 'ont bu'
        }
    },
    'venir': {
        'present': {
            'je': 'viens',
            'tu': 'viens',
            'il': 'vient',
            'elle': 'vient',
            'nous': 'venons',
            'vous': 'venez',
            'ils': 'viennent',
            'elles': 'viennent'
        },
        'passe_compose': {
            'je': 'suis venu',
            'tu': 'es venu',
            'il': 'est venu',
            'elle': 'est venue',
            'nous': 'sommes venus',
            'vous': 'êtes venus',
            'ils': 'sont venus',
            'elles': 'sont venues'
        }
    },
    'croire': {
        'present': {
            'je': 'crois',
            'tu': 'crois',
            'il': 'croit',
            'elle': 'croit',
            'nous': 'croyons',
            'vous': 'croyez',
            'ils': 'croient',
            'elles': 'croient'
        },
        'passe_compose': {
            'je': 'ai cru',
            'tu': 'as cru',
            'il': 'a cru',
            'elle': 'a cru',
            'nous': 'avons cru',
            'vous': 'avez cru',
            'ils': 'ont cru',
            'elles': 'ont cru'
        }
    },
    'produire': {
        'present': {
            'je': 'produis',
            'tu': 'produis',
            'il': 'produit',
            'elle': 'produit',
            'nous': 'produisons',
            'vous': 'produisez',
            'ils': 'produisent',
            'elles': 'produisent'
        },
        'passe_compose': {
            'je': 'ai produit',
            'tu': 'as produit',
            'il': 'a produit',
            'elle': 'a produit',
            'nous': 'avons produit',
            'vous': 'avez produit',
            'ils': 'ont produit',
            'elles': 'ont produit'
        }
    },
    'faire': {
        'present': {
            'je': 'fais',
            'tu': 'fais',
            'il': 'fait',
            'elle': 'fait',
            'nous': 'faisons',
            'vous': 'faites',
            'ils': 'font',
            'elles': 'font'
        },
        'passe_compose': {
            'je': 'ai fait',
            'tu': 'as fait',
            'il': 'a fait',
            'elle': 'a fait',
            'nous': 'avons fait',
            'vous': 'avez fait',
            'ils': 'ont fait',
            'elles': 'ont fait'
        }
    },
    'courir': {
        'present': {
            'je': 'cours',
            'tu': 'cours',
            'il': 'court',
            'elle': 'court',
            'nous': 'courons',
            'vous': 'courez',
            'ils': 'courent',
            'elles': 'courent'
        },
        'passe_compose': {
            'je': 'ai couru',
            'tu': 'as couru',
            'il': 'a couru',
            'elle': 'a couru',
            'nous': 'avons couru',
            'vous': 'avez couru',
            'ils': 'ont couru',
            'elles': 'ont couru'
        }
    },
    'savoir': {
        'present': {
            'je': 'sais',
            'tu': 'sais',
            'il': 'sait',
            'elle': 'sait',
            'nous': 'savons',
            'vous': 'savez',
            'ils': 'savent',
            'elles': 'savent'
        },
        'passe_compose': {
            'je': 'ai su',
            'tu': 'as su',
            'il': 'a su',
            'elle': 'a su',
            'nous': 'avons su',
            'vous': 'avez su',
            'ils': 'ont su',
            'elles': 'ont su'
        }
    },
    'connaitre': {
        'present': {
            'je': 'connais',
            'tu': 'connais',
            'il': 'connait',
            'elle': 'connait',
            'nous': 'connaissons',
            'vous': 'connaissez',
            'ils': 'connaissent',
            'elles': 'connaissent'
        },
        'passe_compose': {
            'je': 'ai connu',
            'tu': 'as connu',
            'il': 'a connu',
            'elle': 'a connu',
            'nous': 'avons connu',
            'vous': 'avez connu',
            'ils': 'ont connu',
            'elles': 'ont connu'
        }
    },
    'devoir': {
        'present': {
            'je': 'dois',
            'tu': 'dois',
            'il': 'doit',
            'elle': 'doit',
            'nous': 'devons',
            'vous': 'devez',
            'ils': 'doivent',
            'elles': 'doivent'
        },
        'passe_compose': {
            'je': 'ai dû',
            'tu': 'as dû',
            'il': 'a dû',
            'elle': 'a dû',
            'nous': 'avons dû',
            'vous': 'avez dû',
            'ils': 'ont dû',
            'elles': 'ont dû'
        }
    },
    'vouloir': {
        'present': {
            'je': 'veux',
            'tu': 'veux',
            'il': 'veut',
            'elle': 'veut',
            'nous': 'voulons',
            'vous': 'voulez',
            'ils': 'veulent',
            'elles': 'veulent'
        },
        'passe_compose': {
            'je': 'ai voulu',
            'tu': 'as voulu',
            'il': 'a voulu',
            'elle': 'a voulu',
            'nous': 'avons voulu',
            'vous': 'avez voulu',
            'ils': 'ont voulu',
            'elles': 'ont voulu'
        }
    },
    'pouvoir': {
        'present': {
            'je': 'peux',
            'tu': 'peux',
            'il': 'peut',
            'elle': 'peut',
            'nous': 'pouvons',
            'vous': 'pouvez',
            'ils': 'peuvent',
            'elles': 'peuvent'
        },
        'passe_compose': {
            'je': 'ai pu',
            'tu': 'as pu',
            'il': 'a pu',
            'elle': 'a pu',
            'nous': 'avons pu',
            'vous': 'avez pu',
            'ils': 'ont pu',
            'elles': 'ont pu'
        }
    },
    'dormir': {
        'present': {
            'je': 'dors',
            'tu': 'dors',
            'il': 'dort',
            'elle': 'dort',
            'nous': 'dormons',
            'vous': 'dormez',
            'ils': 'dorment',
            'elles': 'dorment'
        },
        'passe_compose': {
            'je': 'ai dormi',
            'tu': 'as dormi',
            'il': 'a dormi',
            'elle': 'a dormi',
            'nous': 'avons dormi',
            'vous': 'avez dormi',
            'ils': 'ont dormi',
            'elles': 'ont dormi'
        }
    },
    'ecrire': {
        'present': {
            'je': 'écris',
            'tu': 'écris',
            'il': 'écrit',
            'elle': 'écrit',
            'nous': 'écrivons',
            'vous': 'écrivez',
            'ils': 'écrivent',
            'elles': 'écrivent'
        },
        'passe_compose': {
            'je': 'ai écrit',
            'tu': 'as écrit',
            'il': 'a écrit',
            'elle': 'a écrit',
            'nous': 'avons écrit',
            'vous': 'avez écrit',
            'ils': 'ont écrit',
            'elles': 'ont écrit'
        }
    },
    'lire': {
        'present': {
            'je': 'lis',
            'tu': 'lis',
            'il': 'lit',
            'elle': 'lit',
            'nous': 'lisons',
            'vous': 'lisez',
            'ils': 'lisent',
            'elles': 'lisent'
        },
        'passe_compose': {
            'je': 'ai lu',
            'tu': 'as lu',
            'il': 'a lu',
            'elle': 'a lu',
            'nous': 'avons lu',
            'vous': 'avez lu',
            'ils': 'ont lu',
            'elles': 'ont lu'
        }
    },
    'suivre': {
        'present': {
            'je': 'suis',
            'tu': 'suis',
            'il': 'suit',
            'elle': 'suit',
            'nous': 'suivons',
            'vous': 'suivez',
            'ils': 'suivent',
            'elles': 'suivent'
        },
        'passe_compose': {
            'je': 'ai suivi',
            'tu': 'as suivi',
            'il': 'a suivi',
            'elle': 'a suivi',
            'nous': 'avons suivi',
            'vous': 'avez suivi',
            'ils': 'ont suivi',
            'elles': 'ont suivi'
        }
    },
    'prendre': {
        'present': {
            'je': 'prends',
            'tu': 'prends',
            'il': 'prend',
            'elle': 'prend',
            'nous': 'prenons',
            'vous': 'prenez',
            'ils': 'prennent',
            'elles': 'prennent'
        },
        'passe_compose': {
            'je': 'ai pris',
            'tu': 'as pris',
            'il': 'a pris',
            'elle': 'a pris',
            'nous': 'avons pris',
            'vous': 'avez pris',
            'ils': 'ont pris',
            'elles': 'ont pris'
        }
    },
    'attendre': {
        'present': {
            'je': 'attends',
            'tu': 'attends',
            'il': 'attend',
            'elle': 'attend',
            'nous': 'attendons',
            'vous': 'attendez',
            'ils': 'attendent',
            'elles': 'attendent'
        },
        'passe_compose': {
            'je': 'ai attendu',
            'tu': 'as attendu',
            'il': 'a attendu',
            'elle': 'a attendu',
            'nous': 'avons attendu',
            'vous': 'avez attendu',
            'ils': 'ont attendu',
            'elles': 'ont attendu'
        }
    },
    'mettre': {
        'present': {
            'je': 'mets',
            'tu': 'mets',
            'il': 'met',
            'elle': 'met',
            'nous': 'mettons',
            'vous': 'mettez',
            'ils': 'mettent',
            'elles': 'mettent'
        },
        'passe_compose': {
            'je': 'ai mis',
            'tu': 'as mis',
            'il': 'a mis',
            'elle': 'a mis',
            'nous': 'avons mis',
            'vous': 'avez mis',
            'ils': 'ont mis',
            'elles': 'ont mis'
        }
    },
    'recevoir': {
        'present': {
            'je': 'reçois',
            'tu': 'reçois',
            'il': 'reçoit',
            'elle': 'reçoit',
            'nous': 'recevons',
            'vous': 'recevez',
            'ils': 'reçoivent',
            'elles': 'reçoivent'
        },
        'passe_compose': {
            'je': 'ai reçu',
            'tu': 'as reçu',
            'il': 'a reçu',
            'elle': 'a reçu',
            'nous': 'avons reçu',
            'vous': 'avez reçu',
            'ils': 'ont reçu',
            'elles': 'ont reçu'
        }
    },
    'offrir': {
        'present': {
            'je': 'offre',
            'tu': 'offres',
            'il': 'offre',
            'elle': 'offre',
            'nous': 'offrons',
            'vous': 'offrez',
            'ils': 'offrent',
            'elles': 'offrent'
        },
        'passe_compose': {
            'je': 'ai offert',
            'tu': 'as offert',
            'il': 'a offert',
            'elle': 'a offert',
            'nous': 'avons offert',
            'vous': 'avez offert',
            'ils': 'ont offert',
            'elles': 'ont offert'
        }
    },
    'decouvrir': {
        'present': {
            'je': 'découvre',
            'tu': 'découvres',
            'il': 'découvre',
            'elle': 'découvre',
            'nous': 'découvrons',
            'vous': 'découvrez',
            'ils': 'découvrent',
            'elles': 'découvrent'
        },
        'passe_compose': {
            'je': 'ai découvert',
            'tu': 'as découvert',
            'il': 'a découvert',
            'elle': 'a découvert',
            'nous': 'avons découvert',
            'vous': 'avez découvert',
            'ils': 'ont découvert',
            'elles': 'ont découvert'
        }
    },
    'travailler': {
        'present': {
            'je': 'travaille',
            'tu': 'travailles',
            'il': 'travaille',
            'elle': 'travaille',
            'nous': 'travaillons',
            'vous': 'travaillez',
            'ils': 'travaillent',
            'elles': 'travaillent'
        },
        'passe_compose': {
            'je': 'ai travaillé',
            'tu': 'as travaillé',
            'il': 'a travaillé',
            'elle': 'a travaillé',
            'nous': 'avons travaillé',
            'vous': 'avez travaillé',
            'ils': 'ont travaillé',
            'elles': 'ont travaillé'
        }
    },
    'grandir': {
        'present': {
            'je': 'grandis',
            'tu': 'grandis',
            'il': 'grandit',
            'elle': 'grandit',
            'nous': 'grandissons',
            'vous': 'grandissez',
            'ils': 'grandissent',
            'elles': 'grandissent'
        },
        'passe_compose': {
            'je': 'ai grandi',
            'tu': 'as grandi',
            'il': 'a grandi',
            'elle': 'a grandi',
            'nous': 'avons grandi',
            'vous': 'avez grandi',
            'ils': 'ont grandi',
            'elles': 'ont grandi'
        }
    },
    'reflechir': {
        'present': {
            'je': 'réfléchis',
            'tu': 'réfléchis',
            'il': 'réfléchit',
            'elle': 'réfléchit',
            'nous': 'réfléchissons',
            'vous': 'réfléchissez',
            'ils': 'réfléchissent',
            'elles': 'réfléchissent'
        },
        'passe_compose': {
            'je': 'ai réfléchi',
            'tu': 'as réfléchi',
            'il': 'a réfléchi',
            'elle': 'a réfléchi',
            'nous': 'avons réfléchi',
            'vous': 'avez réfléchi',
            'ils': 'ont réfléchi',
            'elles': 'ont réfléchi'
        }
    },
    'vendre': {
        'present': {
            'je': 'vends',
            'tu': 'vends',
            'il': 'vend',
            'elle': 'vend',
            'nous': 'vendons',
            'vous': 'vendez',
            'ils': 'vendent',
            'elles': 'vendent'
        },
        'passe_compose': {
            'je': 'ai vendu',
            'tu': 'as vendu',
            'il': 'a vendu',
            'elle': 'a vendu',
            'nous': 'avons vendu',
            'vous': 'avez vendu',
            'ils': 'ont vendu',
            'elles': 'ont vendu'
        }
    },
    'entrer': {
        'present': {
            'je': 'entre',
            'tu': 'entres',
            'il': 'entre',
            'elle': 'entre',
            'nous': 'entrons',
            'vous': 'entrez',
            'ils': 'entrent',
            'elles': 'entrent'
        },
        'passe_compose': {
            'je': 'suis entré',
            'tu': 'es entré',
            'il': 'est entré',
            'elle': 'est entrée',
            'nous': 'sommes entrés',
            'vous': 'êtes entrés',
            'ils': 'sont entrés',
            'elles': 'sont entrées'
        }
    },
    'sortir': {
        'present': {
            'je': 'sors',
            'tu': 'sors',
            'il': 'sort',
            'elle': 'sort',
            'nous': 'sortons',
            'vous': 'sortez',
            'ils': 'sortent',
            'elles': 'sortent'
        },
        'passe_compose': {
            'je': 'suis sorti',
            'tu': 'es sorti',
            'il': 'est sorti',
            'elle': 'est sortie',
            'nous': 'sommes sortis',
            'vous': 'êtes sortis',
            'ils': 'sont sortis',
            'elles': 'sont sorties'
        }
    },
    'monter': {
        'present': {
            'je': 'monte',
            'tu': 'montes',
            'il': 'monte',
            'elle': 'monte',
            'nous': 'montons',
            'vous': 'montez',
            'ils': 'montent',
            'elles': 'montent'
        },
        'passe_compose': {
            'je': 'suis monté',
            'tu': 'es monté',
            'il': 'est monté',
            'elle': 'est montée',
            'nous': 'sommes montés',
            'vous': 'êtes montés',
            'ils': 'sont montés',
            'elles': 'sont montées'
        }
    },
    'descendre': {
        'present': {
            'je': 'descends',
            'tu': 'descends',
            'il': 'descend',
            'elle': 'descend',
            'nous': 'descendons',
            'vous': 'descendez',
            'ils': 'descendent',
            'elles': 'descendent'
        },
        'passe_compose': {
            'je': 'suis descendu',
            'tu': 'es descendu',
            'il': 'est descendu',
            'elle': 'est descendue',
            'nous': 'sommes descendus',
            'vous': 'êtes descendus',
            'ils': 'sont descendus',
            'elles': 'sont descendues'
        }
    },
    'se laver': {
        'present': {
            'je': 'me lave',
            'tu': 'te laves',
            'il': 'se lave',
            'elle': 'se lave',
            'nous': 'nous lavons',
            'vous': 'vous lavez',
            'ils': 'se lavent',
            'elles': 'se lavent'
        },
        'passe_compose': {
            'je': 'me suis lavé',
            'tu': 'te es lavé',
            'il': 'se est lavé',
            'elle': 'se est lavée',
            'nous': 'nous sommes lavés',
            'vous': 'vous êtes lavés',
            'ils': 'se sont lavés',
            'elles': 'se sont lavées'
        }
    },
    "s'evanouir": {
        'present': {
            'je': 'me évanouis',
            'tu': 'te évanouis',
            'il': 'se évanouit',
            'elle': 'se évanouit',
            'nous': 'nous évanouissons',
            'vous': 'vous évanouissez',
            'ils': 's\'évanouissent',
            'elles': 's\'évanouissent'
        },
        'passe_compose': {
            'je': 'me suis évanoui',
            'tu': 'te es évanoui',
            'il': 'se est évanoui',
            'elle': 'se est évanouie',
            'nous': 'nous sommes évanouis',
            'vous': 'vous êtes évanouis',
            'ils': 'se sont évanouis',
            'elles': 'se sont évanouies'
        }
    },
    "s'enfuir": {
        'present': {
            'je': 'me enfuis',
            'tu': 'te enfuis',
            'il': 'se enfuit',
            'elle': 'se enfuit',
            'nous': 'nous enfuyons',
            'vous': 'vous enfuyez',
            'ils': 'se enfuient',
            'elles': 'se enfuient'
        },
        'passe_compose': {
            'je': 'me suis enfui',
            'tu': 'te es enfui',
            'il': 'se est enfui',
            'elle': 'se est enfuie',
            'nous': 'nous sommes enfuis',
            'vous': 'vous êtes enfuis',
            'ils': 'se sont enfuis',
            'elles': 'se sont enfuies'
        }
    },
    'se raser': {
        'present': {
            'je': 'me rase',
            'tu': 'te rases',
            'il': 'se rase',
            'elle': 'se rase',
            'nous': 'nous rasions',
            'vous': 'vous rasez',
            'ils': 'se rasent',
            'elles': 'se rasent'
        },
        'passe_compose': {
            'je': 'me suis rasé',
            'tu': 'te es rasé',
            'il': 'se est rasé',
            'elle': 'se est rasée',
            'nous': 'nous sommes rasés',
            'vous': 'vous êtes rasés',
            'ils': 'se sont rasés',
            'elles': 'se sont rasées'
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