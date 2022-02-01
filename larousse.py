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

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }


        embed = {
            "username": f'{nom_webhook}',
            "avatar_url": f"{avatar_webhook}",
            "embeds": [
                {
                        "color": 0xFF0000,
                        "title": f'Nombre de mots : {nombre}',
                        'description': f' {resultat}',
                        "author": {
                            "name": "Choix de mots",
                            'icon-url': 'https://i.imgur.com/wxf30FQ.jpg'
                        },
                    'thumbnail': {
                            'url': avatar_webhook,
                        }
                }]}

        post(lien, data=dumps(embed).encode("utf-8"), headers=headers)

        return True

word_in_webhook(lien='https://discord.com/api/webhooks/932310737425158164/m36x1TJytSNaCH29qqb-S53O0Q6hXsVWZS7zfLkwMot3AtjV9OmElLagPQE3IPsQ0z0e', nombre=2, nom_webhook='Mots')
