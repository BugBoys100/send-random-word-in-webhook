# send-random-word-in-webhook
Send-message-in-webhook est un simple package PyPi permettant d'envoyer des mots aléatoires dans un webhook Discord.

## Pré-requis 😀

Pour pouvoir utiliser Random Word, il vous faut : 

- [Python 3.1](https://www.python.org/downloads/) ou supérieur
- Module [Requests](https://pypi.org/project/requests/) et [Larousse api](https://github.com/quentin-dev/larousse_api)

## Installation 📲

Pour installer Send-random-word-in-webhook, faites `py -m pip install send-random-word-in-webhook` *(prochainement)*

## Utilisation 1️⃣

### Pour utiliser le programme :
- Dans votre script python, importez le module puis appelez la fonction `word_in_webhook()`

### Paramètres 
- `lien` (lien du webhook discord, commençant par `'https://discord.com/api/webhooks/'`), str, __Obligatoire__
- `nombre` (nombre de mots à envoyer), int, __Obligatoire__
- `nom_webhook` (nom du webhook qui sera envoyé), str, __Facultatif__
- `avatar_webhook` (avatar du webhook envoyé), str, __Facultatif__

## Exemple d'utilisation :

```python
from send-random-word-in-webhook import word_in_webhook

word_in_webhook(lien="https://discord.com/api/webhooks/xxxx/xxxx", nombre=2, name_webhook="Mots aléatoires")
```

## Fabriqué avec 🤝

* [Requests](https://pypi.org/project/requests/) - Envoyer la requête d'envoi du webhook
* [Larousse api](https://github.com/quentin-dev/larousse_api) - Chercher la définition d'un mot

## Prochainement ... 🤔

Les modifications ou ajouts à venir :
- Ajout d'une option definition (bool) pour choisir si la définition du mot doit être envoyée ou juste un lien LaRousse

## Auteur ✏️
* **Bug Boys** _alias_ [@BugBoys100](https://github.com/BugBoys100)

## License ©️

Ce projet est sous licence ``Eclipse Public License 2.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations
