import sys
sys.path.append('./Programs')

#-------------------------------------------------------------------------------------------------------------
from convDeTemp import *
from imc import *

#-------------------------------------------------------------------------------------------------------------

print("""   
Ceci est un programme écrit par moi (Rayan I.) afin de montrer mes capacités en développement dans mon CV et autre.
lien profile github: https://github.com/ares1345
-------------------------------------------------
    
    """)

print("""1- Convertisseur de temperatures       
2- Calculateur d'IMC                                   
""")

choix = input("Quel programmes choisissez-vous? (Entrer le numéro du programme) ")
while choix != "-1":
    
    if choix == "1":
        convDeTemp()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

    if choix == "2":
        imc()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

if choix == "-1":
    print()
    quit()