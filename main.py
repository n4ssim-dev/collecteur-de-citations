import requests

# Emet une requete à l'api défini et retourne 
# la réponse à l'utilisateur en JSON
def appel_api():
    api_url = 'http://api.quotable.io/random'
    response =  requests.get(url=api_url)

    if response.status_code == requests.codes.ok:
        r = response.json()

        citation = {
            'auteur': r['author'],
            'contenu':r['content']
        }

    return citation;

citation = appel_api()
print(citation)