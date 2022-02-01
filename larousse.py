# by BugBoys100

def word_in_webhook(nombre:int, definition:bool):
    '''Envoie un nombre (nombre:int) de mots français aléatoires dans un webhook'''

    #load modules
    import random
    from larousse_api import larousse

    # choix du mot
    mots_a_trouver = []
    mots_larousse = []


    for i in range(nombre):
        mot_a_trouver = random.choice(open('liste_francais.txt').readlines())
        mot_a_trouver = mot_a_trouver[:len(mot_a_trouver)-1]
        mots_a_trouver.append(mot_a_trouver)

        if definition:
            temp_def = larousse.get_definitions(mot_a_trouver)
            if len(temp_def) == 0:

                larousse_def = 'Aucune définition'
            else:
                larousse_def = temp_def[0]
            if larousse_def.startswith('1. '): larousse_def = larousse_def[3:]
            mots_larousse.append(larousse_def)

    resultat = ''
    # Infos sur le webhook
    
    if definition:
        for i in range(nombre):
            resultat = resultat + \
                f' \n- **__{mots_a_trouver[i].capitalize()}__** : \n```{mots_larousse[i]}```\n'
    else : 
        for i in range(nombre):
            resultat = resultat + \
            f'\n- **__{mots_a_trouver[i].capitalize()} : https://www.larousse.fr/dictionnaires/francais/{mots_a_trouver[i]}__** \n'

    return resultat