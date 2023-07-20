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
    print(f"Votre IMC est de {res}")
    print()

    if res < 16.5:
        print("Vous êtes en maigreur extrême. ")
    
    elif res > 16.5 and res < 18.5:
        print("Vous êtes en maigreur. ")
    


imc()


