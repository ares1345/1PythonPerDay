import time

def pomodoroTimer():
    print()

    choix = input("Souhaitez-vous utilisez les paramètres par défaut? (O pour oui, N pour non) ")

    if choix.upper() == "O":
        for i in range(4):
            for j in range(1500, 0, -1):
                secondes = j % 60
                minutes = int(j/60) % 60
                heures = int(x/3600)
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

        tempsTr *= 60
        tempsRep *= 60
        for i in range(nbRep):
             

        
            