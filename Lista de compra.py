#nombre cliente
#elementos de productos

import flet as ft

def main(page: ft.Page):
    page.title="Fruteria er Cherry"
    def cambiar_color(e):
        t.value=textField_Nombre.value
        page.update()
    #Componentes texto
    t=ft.Text(value="¿Qué quiere comprar?", color="green", size=50)
    page.add(t) #add hace dos cosas 1-añadir y 2-actualizar

    t.value="¿Qué quiere comprar?"
    page.update()

    #Componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiar_color)
    page.add(bt)

    textField_Nombre=ft.TextField(label="Productos",hint_text="Dime los productos que quieras comprar")
    #page.add(textField_Nombre)

    dropDown_Menu=ft.Dropdown(width=300,label="Productos")
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Carnes"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Verdura"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Fruta"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Droga"))
    page.update()

    slider_edad=ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}")
    #page.add(slider_edad)
    
    fila=ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)



ft.app(target=main)