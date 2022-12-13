#nombre cliente
#elementos de productos

import flet as ft

def main(page: ft.Page):
    page.title="Fruteria er Cherry"
    def añadir_elemento(e):
        t.value=(textField_Nombre.value + "-" + textField_Menu.value)
        print(t.value)
        page.update()

    
    def guardar_elemento(e):
        texto.value = f"Quieres comprar:  {menu.value}"
        page.update()


    #Componentes texto
    t=ft.Text(value="¿Qué quiere comprar?", color="White", size=50)
    page.add(t) #add hace dos cosas 1-añadir y 2-actualizar

    t.value="¿Qué quiere comprar?"
    page.update()

    #Componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=añadir_elemento)
    page.add(bt)

    text_Nombre=ft.TextField(label="Nombre",hint_text="Dime el nombre del comprador")
    #page.add(textField_Nombre)

    texto_Menu = ft.Text()
    boton_guardar = ft.ElevatedButton(text="Confirmar compra", on_click=guardar_elemento)
    menu = ft.Dropdown(label="Productos",width=100,
        options=[ft.dropdown.Option("Frutas"),
                ft.dropdown.Option("Verduras"),
                ft.dropdown.Option("Pescao"),])
            
    page.add(menu, boton_guardar ,texto_Menu)
    
    
    text_Menu=dropDown_Menu=ft.Dropdown(width=300,label="Productos")
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Carnes"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Verdura"))
    page.update()
    dropDown_Menu.options.append(ft.dropdown.Option("Fruta"))
    page.update()

    text_cantidad=slider_cantidad=ft.Slider(min=0, max=20, divisions=20, label="Cantidad: {value}")
    #page.add(slider_cantidad)
    
    fila=ft.Row(controls=[text_Nombre,text_Menu,text_cantidad])
    page.add(fila)



ft.app(target=main)