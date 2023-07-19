import sys
sys.path.append('/home/joe/repos/1PythonPerDay/Programs')
#NOTE: Pour que le programme fonctionne, il faut changer ce PATH avec celui ou est installés le programmes

#-------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------

print("""1- Convertisseur de temperatures       
2- test                                   """)

choix = input("Quel programmes choisissez-vous? ")
while choix != "-1":
    
    if choix == "1":
        
        choix = input("Quel programmes choisissez-vous? ")

if choix == "-1":
    quit()