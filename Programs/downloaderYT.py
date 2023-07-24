from pytube import YouTube as YT
from pytube.cli import on_progress #this module contains the built in progress bar. 

def downloaderYT():
    print()
    print("Ce programme a juste une valeur illustrative pour montrer mes capacités en programmation. Je condamne avec la plus grande fermeté le téléchargement de vidéos sans passer par une manière approuvé par Youtube. ")
    print()
    print()
    lien = input("Veuillez entrer le lien de la vidéo qui sera télécharger dans le dossier 'videos'. ")
    yt = YT(lien, on_progress_callback=on_progress)

    videos= 

downloaderYT()