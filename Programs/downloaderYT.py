from pytube import YouTube as YT
from pytube.cli import on_progress #this module contains the built in progress bar. 

def downloaderYT():
    print()
    print("Ce programme a juste une valeur illustrative pour montrer mes capacités en programmation. Je condamne avec la plus grande fermeté le téléchargement de vidéos sans passer par une manière approuvé par Youtube. ")
    print()
    print()
    lien = input("Veuillez entrer le lien de la vidéo qui sera télécharger dans le dossier 'videos'. ")
    yt = YT(lien, on_progress_callback=on_progress)


    print()
    choix = input("Souhaitez-vous seulement l'audio de la vidéo ou la vidéo entièrement? (veuillez entrer A pour audio et V pour video )")
    while choix.upper() != "A" and choix.upper() != "V":
        choix = input("Erreur, veuillez entrer un choix valide. (A pour audio, V pour vidéo.) ")

    if choix == "A":
        audio = yt.streams.first()
        audio = yt.streams.filter(only_audio=True)
        audio[0].download("./Programs/videos")

    #videos = yt.streams.first()
    #videos = yt.streams.get_highest_resolution

downloaderYT()