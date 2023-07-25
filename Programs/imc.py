def imc():
    print()
    res = 0.0
    poids = int(input("Quelle est votre poids? (en kilo) "))
    unitTaille = input("Quelle est l'unité de la taille que vous comptez utiliser? (M ou CM) ")
    if unitTaille.upper() == "M":
        taille = float(input("Veuillez indiquer votre taille (en M) "))
        res = poids / (taille * taille)
    elif unitTaille.upper() == "CM":
        taille = int(input("Quelle est votre taille (en CM) "))
        taille/= 100
        res = poids / (taille * taille)
    res = float("{:.2f}".format(res))
    print()
    print()
    print(f"Votre IMC est de {res}")
    print()

    if res < 16.5:
        print("Vous êtes en maigreur extrême. ")
    
    elif res > 16.5 and res < 18.5:
        print("Vous êtes en maigreur. ")
    
    elif res > 18.5 and res < 25:
        print("Vous avez une corpulence normal. ")

    elif res > 25 and res < 30:
        print("Vous êtes en surpoids. ")

    elif res > 30 and res < 35:
        print("Vous êtes en obésité modéréee. ")
    
    elif res > 35 and res < 40:
        print("Vous êtes en obésité sévère. ")

    print("""
    
        Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)





