import requests

# Emet une requete à l'api défini et retourne 
# la réponse à l'utilisateur en JSON
def appel_api(nbCitations: int):
    api_url : str = 'http://api.quotable.io/random'
    citations : list = []

    for i in range (nbCitations):
    
        response =  requests.get(url=api_url)

        if response.status_code == requests.codes.ok:
            r = response.json()

            citation = {
                'id': i,
                'auteur': r['author'],
                'contenu':r['content']
            }

            citations.append(citation)
            i+=1

    return citations;

citations = appel_api(5)
count = 0

for citation in citations:
    print(f'{citations[count]}\n\n')
    count += 1
