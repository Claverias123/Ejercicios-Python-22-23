from pytube import Playlist

def descargarLista(url:str):
    playlist=Playlist(url)
    for cancion in playlist:
        print(cancion)

url="https://www.youtube.com/watch?v=kgcm0_wxHFQ&list=PLVZtocpycmEUbKbqDt1bnnA67njRJHZll"
descargarLista(url)
