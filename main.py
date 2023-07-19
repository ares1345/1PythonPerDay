import sys
sys.path.append('/home/joe/repos/1PythonPerDay/Programs')
#NOTE: Pour que le programme fonctionne, il faut changer ce PATH avec celui ou est installés le programme et surtout celui qui mène au dossier Programs

#-------------------------------------------------------------------------------------------------------------
from convDeTemp import *


#-------------------------------------------------------------------------------------------------------------

print("""   
Ceci est un programme écrit par moi (Rayan I.) afin de montrer mes capacités en développement dans mon CV et autre.
lien profile github: https://github.com/ares1345
-------------------------------------------------
    
    """)

print("""1- Convertisseur de temperatures       
2- test                                   
""")

choix = input("Quel programmes choisissez-vous? (Entrer le numéro du programme) ")
while choix != "-1":
    
    if choix == "1":
        convDeTemp()
        choix = input("Quel programmes choisissez-vous? (Si vous souhaitez quitter le programme, entrer -1) ")

if choix == "-1":
    quit()