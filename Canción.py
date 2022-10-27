from pytube import YouTube
from pytube import Playlist




def descargaCancion(url:str):
    youtube=YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

descargaCancion("https://www.youtube.com/shorts/vCiukaljhO4")




