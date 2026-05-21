# Collecteur de citations

> Un outil Python qui récupère automatiquement des citations depuis une API publique et génère une page HTML stylisée pour les présenter.

---

## Présentation

**Collecteur de citations** est un projet pédagogique combinant :

- la consommation d'une API REST,
- le traitement de données structurées,
- la génération de contenu web statique.

L'objectif est de produire une page HTML visuellement soignée à partir de citations récupérées dynamiquement.

---

## Consignes de lancement

- Executer le script 'main.py'
- Ouvrir le fichier 'output.html' à 'http://127.0.0.1:3000/output.html'
- 5 nouvelles citations sont générer à chaque fois que le script est executé et que la page est rafraîchis


---

## Notions abordées

- Les appels HTTP
- La manipulation de données JSON
- La génération automatique de contenu HTML
- Une première approche de l'automatisation de production web

---

## Modalités d'évaluation

- la récupération correcte des données API ;
- la compréhension et l'exploitation du JSON ;
- la génération automatique du HTML ;
- la qualité générale de la page produite ;
- la clarté du code Python ;
- la bonne utilisation de Git pendant le travail collaboratif.

---

## Étapes du projet

1. **Requête initiale** — émettre un appel à l'API fournie
2. **Parsing** — transformer les données JSON en dictionnaires Python exploitables
3. **Template HTML** — produire une structure HTML avec Python sur laquelle mapper les données
4. **Mise en forme** — styliser la page produite avec du CSS
