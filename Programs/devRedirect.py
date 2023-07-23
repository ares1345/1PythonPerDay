import webbrowser
#webbrowser.open("https://google.com")

def devRedirect():
    print()
    print("Ceci est un hub de liens intéressent pour la programmation. ")
    print()
    choix = int(input("Quel sujet vous intérsse-t-il aujourd'hui? (1 pour développement web, 2 pour python) "))
    while (choix != 1) and (choix != 2):
        print()
        choix = input("Erreur. Veuillez rentrez un choix valide. ")
    
    if choix == 1:
        choixLien = int(input("""Vous pouvez choisir le nombre associé au site pour être redirigé au site avec votre navigateur
        
        freecodecamp.org (1):
            Une très bonne ressource pour commencer le développement web, mais qui vous prend par la mains, il se pourrait donc que vous n'aimiez par ce que vous êtes en train de créer.
        
        theodinproject.com (2):
            La ressource que j'ai utilisé pour commencer le développement web, ce site vous entraîne au bonnes pratiques d'un développeur (github, technique pomodoro), peut être plus difficile car vous êtes données plus de libertés, vous devez quand même faire le projet mais vous pouvez le faire de votre manière. 
            
        education.github.com (3):
            Pack d'offres partenaires de Github, il vous faut simplement prouver que vous êtes étudiants, peu importe votre niveau de scolarité. Je vous recommende si vous préferer les outils de Jetbrain ou souhaitez apprendre le développement web en général avec des sites plus établis (Frontend Masters, Educative...) et d'autres outils pour vous aidez au mieux.
        
        """))

        while choixLien != 1 and choixLien != 2 and choixLien != 3:
            choixLien = int(input("Erreur. Veuillez entrer un choix valide. "))

        if choixLien == 1:
            webbrowser.open("https://freecodecamp.org")
        elif choixLien == 2:
            webbrowser.open("https://theodinproject.com")
        elif choixLien == 3:
            webbrowser.open("https://education.github.com")

    if choix == 2:
        choixLien = int(input("""Vous pouvez choisir le nombre associé au site pour être redirigé au site avec votre navigateur
        
        sololearn.com (1):
            Une ressource qui peut vous apprendre n'importe quel langage de programmation sur une application. À noter que certaines fonctionnalités sont dérrières un paywall.    
        
        100 days of python par Dr. Angela Yu (Udemy) [udemy.com/course/100-days-of-code/] (2):
            Connu pour son bootcamp sur le développement web, Angela Yu a aussi un cours sur Python mais qui est instruit différament. Au lieu d'écouter des cours, vous codez chaque jour un projet différent et qui vous permet de vous instruire sur python avec de la pratique. À noter que ce cours est payant.

            
        education.github.com (3):
            Pack d'offres partenaires de Github, il vous faut simplement prouver que vous êtes étudiants, peu importe votre niveau de scolarité. Je vous recommende de l'utiliser si vous préferer les outils de Jetbrain ou souhaitez apprendre le développement web en général avec des sites plus établis (Frontend Masters, Educative...) et d'autres outils pour vous aidez au mieux.
        
        """))

        while choixLien != 1 and choixLien != 2 and choixLien != 3:
            choixLien = int(input("Erreur. Veuillez entrer un choix valide. "))

        if choixLien == 1:
            webbrowser.open("https://sololearn.com")
        elif choixLien == 2:
            webbrowser.open("https://www.udemy.com/course/100-days-of-code/")
        elif choixLien == 3:
            webbrowser.open("https://education.github.com")

    print("""
    
    Le programme est terminé, Vous allez être redirigé vers le programme principal
           -------------------------------------------------------------------------
         """)
    

devRedirect()