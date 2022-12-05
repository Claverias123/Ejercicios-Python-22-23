import flet as ft


def main(page: ft.Page):
    page.title="Flet>Tkinter"
    def cambiar_color(e):
        t.value=textField_Nombre.value
        page.update()
    #Componentes texto
    t=ft.Text(value="Introduccion de flet", color="pink", size=133)

    page.add(t) #add hace dos cosas 1-añadir y 2-actualizar

    t.value="Medrano==Dembele"
    page.update()

    #Componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiar_color)
    page.add(bt)

    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    



ft.app(target=main)