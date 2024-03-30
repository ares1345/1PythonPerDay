import sys
sys.path.append('./Programs')


#-------------------------------------------------------------------------------------------------------------

from convDeTemp import *
from imc import *
from ppc import *
from calcDepense import *
from devRedirect import *
from pomodoroTimer import *

#-------------------------------------------------------------------------------------------------------------

print("""   
Ceci est le programme principal écrit par moi afin de montrer mes capacités en développement dans mon CV et autre.
Vous pouvez accéder au autres programmes depuis ce menu.
lien profile github: https://github.com/ray-FR
-------------------------------------------------
    
    """)

print("""1- Convertisseur de temperatures            6-Téléchargeur de vidéos Youtube      
2- Calculateur d'IMC                        7- Timer pomodoro
3- Jeu Pierre Papier Ciseau
4- Calculateur de dépense    
5- Ensemble de lien lié à la programmation                          
""")

choix = input("Quel programmes choisissez-vous? (Entrer le numéro du programme) ")
while choix != "-1":
    
    if choix == "1":
        convDeTemp()
        
    elif choix == "2":
        imc()
        
    elif choix == "3":
        ppc()

    elif choix == "4":
        calcDepense()

    elif choix == "5":
        devRedirect()

    elif choix == "6":
        print("Je suis désolé de vous dire ca mais le programme refuse de se lancer si il n'est pas lancé depuis son fichier.. Si vous voulez l'utilisez vous devez lancer downloaderYT.py vous-même. ")

    elif choix == "7":
        pomodoroTimer()

    
    choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")


print()
quit()
