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


#---------------------------------
#-------      Template       -----
#---------------------------------

template = open("template.html").read()
cards = ""

for citation in citations:
    card = f'<div class="card"><div class="container"><p>{citation["contenu"]}</p><hr><h4><b>{citation["auteur"]}</b></h4></div></div>'
    cards += card + "\n        "

html = template.replace("INSERT-CARDS", cards)

# Génération d'une copie de template.html avec les cards ajoutés 
# à chaque fois que main.py est executé
with open("output.html", "w") as fp:
    fp.write(html)