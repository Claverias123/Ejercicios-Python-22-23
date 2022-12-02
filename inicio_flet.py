import flet as ft


def main(page: ft.Page):
    page.title="Flet>Tkinter"
    def cambiar_color(e):
        for i in range(10):
            text=ft.Text(value=f"Texto numero{i}", size=30)
            page.add(text)
    #Componentes texto
    t=ft.Text(value="Introduccion de flet", color="pink", size=133)

    page.add(t) #add hace dos cosas 1-añadir y 2-actualizar

    t.value="Medrano==Dembele"
    page.update()

    #Componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiar_color)
    page.add(bt)
    



ft.app(target=main)