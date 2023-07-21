import random

def ppc():
    scoreUser = 0
    scoreProg = 0
    print()
    nbPartie = int(input("Combien de partie souhaitez-vous jouer? "))
    while nbPartie <= 0:
        nbPartie = int(input("Erreur, le nombre de partie que vous avez entrés est égal à 0 ou est un nombre négatif, veuillez réessayez"))
    
    for i in range(nbPartie):
        choixUser = input("Que choisissez-vous, pierre, papier ou ciseau? ")
        choixProg = range.randint(1, 3)
        if (choixUser.upper() == "PIERRE" and choixProg == 3) or (choixUser.upper() == "PAPIER" and choixProg == 1) or (choixUser.upper() == "CISEAU" and choixProg == 2):
            print()
            print(f"Vous avez gagné! ")
            print(choixProg)
            print()
            scoreUser += 1

        if (choixUser.upper() == "PIERRE" and choixProg == 2) or (choixUser.upper() == "PAPIER" and choixProg == 3) or (choixUser.upper() == "CISEAU" and choixProg == 1):
            print()
            print(f"Vous avez perdu! ")
            print(choixProg)
            print()
            scoreProg += 1

    if scoreUser > scoreProg:
        print("""
        -----------------
        
            Vous avez gagné! """)
    
    elif scoreUser < scoreProg:
        print("""
        -----------------
        
            Vous avez gagné! """)
        
    elif scoreUser == scoreProg:
        print("""
        -----------------
        
            Égalité! """)



    print("""
    
    Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)

ppc()
        

