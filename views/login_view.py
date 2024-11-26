from flet import Page, Column, Text, TextField, ElevatedButton, AlertDialog, View
from views.dashboard_view import show_dashboard_view
from views.create_view import show_create_view
from views.utils import show_message, show_error
from database import validar_credenciales


def show_login_view(page):
    def login_clicked(e):
        username = username_field.value
        password = password_field.value

        if not username or not password:
            show_message(page, "Todos los campos son obligatorios")
            return
        
        id = validar_credenciales(username,password)
        if id:
            show_dashboard_view(page, id)
        else:
            show_error(page, "Credenciales inválidas, intenta de nuevo.")
               
    def signup_clicked(e):
        show_create_view(page)
    username_field = TextField(label="Usuario", width=300)
    password_field = TextField(label="Contraseña", password=True, width=300)

    login_button = ElevatedButton("Iniciar Sesión", on_click=login_clicked)
    signup_button = ElevatedButton("Crear Cuenta", on_click=signup_clicked)

    page.views.clear()
    page.views.append(
        View(
            "/login",
            controls=[
                Column(
                    [
                        Text("Inicio de Sesión", size=24, weight="bold"),
                        username_field,
                        password_field,
                        login_button,
                        signup_button
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

