import random

def ppc():
    scoreUser = 0
    scoreProg = 0
    print()
    nbPartie = int(input("Combien de partie souhaitez-vous jouer? "))
    while nbPartie <= 0:
        nbPartie = int(input("Erreur, le nombre de partie que vous avez entrés est égal à 0 ou est un nombre négatif, veuillez réessayez. "))
    
    for i in range(nbPartie):
        choixUser = input("Que choisissez-vous, pierre, papier ou ciseau? ")
        choixProg = random.randint(1, 3)
        if (choixUser.upper() == "PIERRE" and choixProg == 3) or (choixUser.upper() == "PAPIER" and choixProg == 1) or (choixUser.upper() == "CISEAU" and choixProg == 2):
            scoreUser += 1
            print()
            print(f"Vous avez gagné! ")
            print()
            

        elif (choixUser.upper() == "PAPIER" and choixProg == 3) or (choixUser.upper() == "PIERRE" and choixProg == 2) or (choixUser.upper() == "CISEAU" and choixProg == 1):
            scoreProg += 1
            print()
            print(f"Vous avez perdu! ")
            print()

        elif (choixUser.upper() == "PAPIER" and choixProg == 2) or (choixUser.upper() == "PIERRE" and choixProg == 1) or (choixUser.upper() == "CISEAU" and choixProg == 3):
            scoreProg += 1
            scoreUser += 1
            print()
            print(f"Égalité! ")
            print()
            

    if scoreUser > scoreProg:
        print(f"""
        -----------------
        
            Vous avez gagné! 

            Votre score: {scoreUser}
            Score du programme: {scoreProg} """)
    
    elif scoreUser < scoreProg:
        print(f"""
        -----------------
        
            Vous avez perdu!

            Votre score: {scoreUser}
            Score du programme: {scoreProg} """)
        
    elif scoreUser == scoreProg:
        print(f"""
        -----------------
        
            Égalité!

            Votre score: {scoreUser}
            Score du programme: {scoreProg} """)



    print("""
    
    Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)

        
