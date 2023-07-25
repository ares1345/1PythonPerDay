import time

def pomodoroTimer():
    print()
    print("""Veuillez noter que ce problème n'est pas entièrement terminée et ne reflète pas exactement l'entièreté de la technique pomodoro. Ce programme ne comprend que la base pour la technique pomodoro et n'a que pour but de montrer mes capacités.
    article sur la technique pomodoro: https://fr.wikipedia.org/wiki/Technique_Pomodoro  """)
    print()

    choix = input("Souhaitez-vous utilisez les paramètres par défaut? (O pour oui, N pour non) ")

    if choix.upper() == "O":
        print("Le mode par défaut est 25 minutes de travail et 5 minutes de pause, répétée 4 fois")
        for i in range(4):
            for j in range(1500, 0, -1):
                secondes = j % 60
                minutes = int(j/60) % 60
                heures = int(j/3600)
                print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")
                time.sleep(1)
            
            print()
            print("PÉRIODE DE TRAVAIL TERMINÉ, 5 MINUTES DE REPOS COMMENCE")
            
            for k in range(300, 0, -1):
                    secondes = k % 60
                    minutes = int(k/60) % 60
                    heures = int(k/3600)
                    print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")
                    time.sleep(1)
            
            print()
            print("PÉRIODE DE REPOS TERMINÉ, PÉRIODE DE 25 MINUTES DE TRAVAIL COMMENCE ")
        



    if choix.upper() == "N":
        tempsTr = int(input("Combien de minutes pour votre période de travail? "))
        tempsRep = int(input("Combien de minutes pour votre période de repos? "))
        nbRep = int(input("Combien de fois souhaitez-vous répéter le temps de travail? "))
        print()

        tempsTr *= 60
        tempsRep *= 60
        for i in range(nbRep):
            for j in range(tempsTr, 0, -1):
                secondes = j % 60
                minutes = int(j/60) % 60
                heures = int(j/3600)
                print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")
                time.sleep(1)
            
            print()
            print(f"PÉRIODE DE TRAVAIL TERMINÉ, {int(tempsRep/60)} MINUTES DE REPOS COMMENCE")
            
            for k in range(tempsRep, 0, -1):
                    secondes = k % 60
                    minutes = int(k/60) % 60
                    heures = int(k/3600)
                    print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")
                    time.sleep(1)
            
            print()
            print(f"PÉRIODE DE REPOS TERMINÉ, PÉRIODE DE {int(tempsTr/60)} MINUTES DE TRAVAIL COMMENCE ")

    print("""
    
        Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)
        

            