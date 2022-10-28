from pytube import YouTube
from pytube import Playlist




def descargaCancion(url:str):
    youtube=YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

descargaCancion("https://www.youtube.com/shorts/vCiukaljhO4")


def descargarLista(url:str):
    playlist=Playlist(url)
    for cancion in playlist.videos:
        print("Descargando cancion:", cancion.title)
        cancion.streams.get_audio_only().download("cancion/")
        print("*************************\n")
url="https://www.youtube.com/watch?v=kgcm0_wxHFQ&list=PLVZtocpycmEUbKbqDt1bnnA67njRJHZll"
descargarLista(url)


