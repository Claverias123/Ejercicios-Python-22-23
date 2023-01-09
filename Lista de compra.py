#nombre cliente
#elementos de productos

import flet as ft

def main(page: ft.Page):
    page.title="Fruteria er Cherry"
    def añadir_elemento(t):
        t.value=(text_Nombre.value + "-" + text_Menu.value)
        print(t.value)
        page.update()

    
    def guardar_elemento(menu):
        menu.value = f"Quieres comprar:  {menu.value}"
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


    
    boton_guardar = ft.ElevatedButton(text="Confirmar compra", on_click=guardar_elemento)
    page.update()
    text_Menu=ft.TextField(label="")
    menu = ft.Dropdown(label="Productos",width=300,
        options=[ft.dropdown.Option("Frutas"),
                ft.dropdown.Option("Verduras"),
                ft.dropdown.Option("Pescao"),])
            


    text_cantidad=slider_cantidad=ft.Slider(min=0, max=20, divisions=20, label="Cantidad: {value}")
    #page.add(slider_cantidad)
    
    fila=ft.Row(controls=[text_Nombre,menu,text_cantidad,])
    fila1=ft.Row(controls=[boton_guardar])
    page.add(fila, fila1)
    img = ft.Image(
        src=f"https://hermanosmarinchiclana.es/wp-content/uploads/2021/07/DSC01779-scaled.jpg",
        width=400,
        height=400,
        fit=ft.ImageFit.CONTAIN)


    page.add(img)

    



ft.app(target=main)