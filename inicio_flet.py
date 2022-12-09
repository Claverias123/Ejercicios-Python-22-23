import flet as ft


def main(page: ft.Page):
    page.title="Flet>Tkinter"
    def cambiar_color(e):
        t.value=textField_Nombre.value
        page.update()
    #Componentes texto
    t=ft.Text(value="Introduccion de flet", color="pink", size=133)
    page.add(t) #add hace dos cosas 1-añadir y 2-actualizar

    t.value="Medri>>>Asensio"
    page.update()

    #Componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiar_color)
    page.add(bt)

    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe el mejor jugador")
    page.add(textField_Nombre)

    dropDown_Menu=ft.Dropdown(width=300,  options=[ft.dropdown.Option("Medrano")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Nueva"))
    page.update()

    slider_edad=ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}")
    page.add(slider_edad)

    fila=ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)



ft.app(target=main)