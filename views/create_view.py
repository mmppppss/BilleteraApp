from os import name
from flet import Page, Column, Text, TextField, ElevatedButton, AlertDialog, View, Dropdown, dropdown
from database import getMoney, createUSuarioWallet
from views.utils import show_message

def show_create_view(page):
    def signup_clicked(e):
        nombre = nombre_field.value
        apellidos = apellidos_field.value
        username = username_field.value
        password = password_field.value
        repeat_password = repeat_password_field.value
        if not username or not password or not repeat_password:
            show_message(page, "Todos los campos son obligatorios")
            return
        
        if password != repeat_password:
            show_message(page, "Las contraseñas no coinciden")
            return

        if createUSuarioWallet(username, password, nombre, apellidos, money_field.value.split(" - ")[0]):
            show_message(page, "Cuenta creada con exito, por favor inicia sesión")
            from views.login_view import show_login_view  
            show_login_view(page)

    def login_clicked(e):
        from views.login_view import show_login_view  # Importación dentro de la función
        show_login_view(page)
   

    username_field = TextField(label="Usuario", width=300)
    password_field = TextField(label="Contraseña", password=True, width=300)
    repeat_password_field = TextField(label="Repetir Contraseña", password=True, width=300)
    nombre_field = TextField(label="Nombre", width=300)
    apellidos_field = TextField(label="Apellido", width=300)
    money = getMoney();

    money_field=Dropdown(
        label="Moneda",
        width=300,
        options=[],
    )
    if money:
        for moneda in money:
            nuevo_elemento = f"{moneda['id']} - {moneda['name']} - {moneda['abrev']}"
            money_field.options.append(dropdown.Option(text=nuevo_elemento ,key=moneda["id"]))

    # Botón de inicio de sesión
    signup_button = ElevatedButton("Crear Cuenta", on_click=signup_clicked)
    login_button = ElevatedButton("Volver a Iniciar Sesión", on_click=login_clicked)

    page.views.clear()
    page.views.append(
        View(
            "/create",
            controls=[
                Column(
                    [
                        Text("Crear Cuenta", size=24, weight="bold"),
                        nombre_field,
                        apellidos_field,
                        username_field,
                        password_field,
                        repeat_password_field,
                        money_field,
                        signup_button,
                        login_button,
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                )
            ],
            vertical_alignment="center",
            horizontal_alignment="center",
        )
    )
    page.update()

