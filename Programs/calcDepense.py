def calcDepense():
    print()
    depense = 0
    total = 0
    while depense != -1:
        depense = float(input("Quelle est la dépense? (entrer -1 si vous avez terminé.) "))
        total += depense
    print()
    print(f"Le total de vos dépenses est de {total}. ")
    print("""
    
    Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)
    
