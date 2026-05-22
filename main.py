import requests

# Emet une requete à l'api défini et retourne 
# la réponse à l'utilisateur en JSON
def appel_api(nbCitations: int):
    api_url : str = f'http://api.quotable.io/quotes/random?limit={nbCitations}'

    response =  requests.get(url=api_url)

    if response.status_code == requests.codes.ok:
        citations = response.json()

    return citations;

citations = appel_api(5)
count = 0

#---------------------------------
#-------      Template       -----
#---------------------------------

template = open("template.html").read()
cards = ""

for i in range(len(citations)):
    card = f'<div class="card"><div class="container"><p>{citations[i]["content"]}</p><hr><h4><b>{citations[i]["author"]}</b></h4></div></div>'
    cards += card + "\n        "

html = template.replace("INSERT-CARDS", cards)

# Génération d'une copie de template.html avec les cards ajoutés 
# à chaque fois que main.py est executé
with open("output.html", "w") as fp:
    fp.write(html)