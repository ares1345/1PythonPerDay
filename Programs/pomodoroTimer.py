import time

def pomodoroTimer():
    defaut = 1500
    defautRep = 4
    defautRepot = 5
    longDefautRepot = 15

    choix = input("Souhaitez-vous utilisez les paramètres par défaut? (O pour oui, N pour non) ")

    if choix.upper() == "O":
        for i in range(1500, 0, -1):
            secondes = i % 60
            