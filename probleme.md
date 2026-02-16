# Problème — Exercice Python 1.2 : Calculateur d’âge (Age Calculator)

## Objectif
Créer un programme Python qui demande **l’année de naissance** de l’utilisateur et calcule son **âge approximatif**.

## Consignes
Ton programme doit :
1. Demander à l’utilisateur son **année de naissance** (entier).
2. Récupérer l’**année courante** (indice : `datetime.date.today().year`).
3. Calculer l’**âge** = année courante − année de naissance.
4. Afficher le résultat avec une phrase claire.

### Bonus (facultatif)
Gérer le cas où l’utilisateur **n’a pas encore fêté son anniversaire** cette année (nécessite de demander jour/mois).
Pour cet exercice de base, on **suppose que l’anniversaire est déjà passé**.

## Exemple d’interaction (format)
Entrée :
- 2000

Sortie (exemple) :
```
Enter your birth year: 2000
--------------------
Current Year: 2025
You are approximately 25 years old.
```

> Remarque : l’année affichée dépend de la date actuelle (le programme doit récupérer l’année courante automatiquement).

## Tester localement
```bash
pip install -r requirements.txt
pytest -q
```

## Exécuter le programme
```bash
python age_calculator.py
```
