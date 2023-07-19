def convDeTemp():
    print("")
    typechoix = input("Quelle type de température souhaitez vous convertir? (C pour celsius ou F pour fahrenheit) ")
    
    temp = float(input("Quel est la température? "))
    
    
    while type(temp) != float:
        temp = float(input("Erreur. Le résultat n'est pas un nombre, veuillez réessayez. "))
    
    
    if typechoix.upper() == "C":
        temp = (temp * 9/5) + 32
        print(f"""La température en Fahrenheit est de {temp}.
        
        Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)
    
    
    if typechoix.upper() == "F":
        temp = (temp - 32) * 5/9
        print(f"""La température en celsius est de {temp}.
         
        Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)
        



    
