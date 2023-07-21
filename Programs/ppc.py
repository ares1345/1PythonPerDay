import random

def ppc():
    print()
    nbPartie = int(input("Combien de partie souhaitez-vous jouer? "))
    while nbPartie <= 0:
        nbPartie = int(input("Erreur, le nombre de partie que vous avez entrés est égal à 0 ou est un nombre négatif, veuillez réessayez"))
    choixUser = input("Que choisissez-vous, pierre, papier ou ciseau?")