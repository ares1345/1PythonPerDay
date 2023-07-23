import sys
sys.path.append('./Programs')

#-------------------------------------------------------------------------------------------------------------

from convDeTemp import *
from imc import *
from ppc import *
from calcDepense import *

#-------------------------------------------------------------------------------------------------------------

print("""   
Ceci est le programme principal écrit par moi (Rayan I.) afin de montrer mes capacités en développement dans mon CV et autre.
Vous pouvez accéder au autres programmes depuis ce menu.
lien profile github: https://github.com/ares1345
-------------------------------------------------
    
    """)

print("""1- Convertisseur de temperatures       
2- Calculateur d'IMC    
3- Jeu Pierre Papier Ciseau
4- Calculateur de dépense                              
""")

choix = input("Quel programmes choisissez-vous? (Entrer le numéro du programme) ")
while choix != "-1":
    
    if choix == "1":
        convDeTemp()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

    elif choix == "2":
        imc()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

    elif choix == "3":
        ppc()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

    elif choix == "4":
        calcDepense()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

if choix == "-1":
    print()
    quit()