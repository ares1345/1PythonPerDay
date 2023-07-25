import time

def pomodoroTimer():
    defaut = 1500
    defautRep = 4
    defautRepot = 5
    longDefautRepot = 15

    choix = input("Souhaitez-vous utilisez les paramètres par défaut? (O pour oui, N pour non) ")

    if choix.upper() == "O":
        for i in range(4):
            for j in range(1500, 0, -1):
                secondes = j % 60
                minutes = int(j/60) % 60
                heures = int(x/3600)
                print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")
                time.sleep(1)
            
            