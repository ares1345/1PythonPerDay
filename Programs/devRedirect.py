import webbrowser
#webbrowser.open("https://google.com")

def devRedirect():
    print()
    print("Ceci est un hub de liens intéressent pour la programmation. ")
    print()
    choix = int(input("Quel sujet vous intérsse-t-il aujourd'hui? (1 pour développement web, 2 pour python) "))
    while choix != 1 or choix != 2:
        print()
        choix = int(input("Erreur. Veuillez rentrez un choix valide. "))
    
    if choix == 1:
        choixLien = int(input("""Vous pouvez choisir le nombre associé au site pour être redirigé au site avec votre navigateur
        freecodecamp.org (1):
            Une très bonne ressource pour commencer le développement web, mais qui vous prend par la mains, il se pourrait donc que vous n'aimiez par ce que vous êtes en train de créer.
        
        theodinproject.com (2):
            La ressource que j'ai utilisé pour commencer le développement web, ce site vous entraîne au bonnes pratiques d'un développeur (github, technique pomodoro), peut être plus difficile car vous êtes données plus de libertés, vous devez quand même faire le projet mais vous pouvez le faire de votre manière. 
            
        education.github.com (3):
            Pack d'offres partenaires de Github, il vous faut simplement prouver que vous êtes étudiants, peu importe votre niveau de scolarité. Je vous recommende si vous préferer les outils de Jetbrain ou souhaitez apprendre le développement web en général avec des sites plus établis (Frontend Masters, Educative...) et d'autres outils pour vous aidez au mieux.
        
        """))