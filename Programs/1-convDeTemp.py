def convDeTemp():
    typechoix = input("Quelle type de température souhaitez vous convertir? (C pour celsius ou F pour fahrenheit)")
    temp = float(input("Quel est la température? "))
    while type(temp) != int or float:
        temp = float(input("Erreur. Le résultat n'est pas un nombre, veuillez réessayez. "))
    if typechoix == "C":
        temp = (temp * 9/5) + 32
        print(f"La température en Fahrenheit est de {temp}. ")
    else:
        temp = (temp - 32) * 5/9
        print(f"La température en celsius est de {temp}. ")

    return """Le p"""
