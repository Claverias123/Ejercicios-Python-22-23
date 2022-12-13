import flet as ft

def main(page: ft.Page):
    def guardar_elemento(e):
        texto.value = f"Quieres comprar:  {menu.value}"
        page.update()

    texto = ft.Text()
    boton_guardar = ft.ElevatedButton(text="Confirmar compra", on_click=guardar_elemento)
    menu = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Frutas"),
            ft.dropdown.Option("Verduras"),
            ft.dropdown.Option("Pescao"),
        ],
    )
    page.add(menu, boton_guardar ,texto)

ft.app(target=main)