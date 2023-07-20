def imc():
    print()
    res = 0.0
    poids = int(input("Quelle est votre poids? (en kilo) "))
    unitTaille = input("Quelle est l'unité de la taille que vous comptez utiliser? (M ou CM) ")
    if unitTaille == "M":
        taille = float(input("Veuillez indiquer votre taille (en M) "))
        res = poids / (taille * taille)
    elif unitTaille == "CM":
        taille = int(input("Quelle est votre taille (en CM) "))
        taille/= 100
        res = poids / (taille * taille)
    print()
    print(f"Votre IMC est de {res}")


