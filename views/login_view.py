from flet import Page, Column, Text, TextField, ElevatedButton, AlertDialog, View
from views.dashboard_view import show_dashboard_view
def show_login_view(page):
    def login_clicked(e):
        username = username_field.value
        password = password_field.value

        # Validar credenciales (aquí puedes conectar con tu base de datos)
        if username == "admin" and password == "1234":
            # Navegar al dashboard
            #codigo que viene luego del login
            show_dashboard_view(page)
        else:
            # Mostrar un error si las credenciales son incorrectas
            page.dialog = AlertDialog(
                title=Text("Error de inicio de sesión"),
                content=Text("Credenciales inválidas, intenta de nuevo."),
                actions=[
                    ElevatedButton("Cerrar", on_click=close_dialog)
                ],
            )
            page.dialog.open = True
            page.update()

    def close_dialog(e):
        # Cierra el diálogo cuando se hace clic en el botón "Cerrar"
        page.dialog.open = False
        page.update()

    # Campos de entrada
    username_field = TextField(label="Usuario", width=300)
    password_field = TextField(label="Contraseña", password=True, width=300)

    # Botón de inicio de sesión
    login_button = ElevatedButton("Iniciar Sesión", on_click=login_clicked)

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

