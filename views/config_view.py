from flet import (
    Page, View, Column, Text, TextField, ElevatedButton, Divider, AlertDialog
)
from views.utils import show_error, show_message

def show_config_view(page: Page, user_data):
    username = TextField(label="Nombre de Usuario", value=user_data["username"])
    nombres = TextField(label="Nombre", value=user_data["nombre"])
    apellidos = TextField(label="Apellidos", value=user_data["apellidos"])
    old_password = TextField(label="Contraseña Actual", password=True, can_reveal_password=True)
    new_password = TextField(label="Nueva Contraseña", password=True, can_reveal_password=True)
    confirm_password = TextField(label="Confirmar Contraseña", password=True, can_reveal_password=True)

    message_dialog = AlertDialog(modal=True)

    def save_changes(e):
        if new_password.value and new_password.value != confirm_password.value:
            show_message("Error", "La nueva contraseña no coincide con la confirmación.")
            return

        updated_data = {
            "username": username.value,
            "nombres": nombres.value,
            "apellidos": apellidos.value,
            "password": new_password.value if new_password.value else None,
        }
        show_message("Éxito", "¡Los cambios se han guardado correctamente!")

    page.views.clear()
    page.views.append(
        View(
            "/configuracion",
            controls=[
                Column(
                    [
                        Text("Configuración de la Cuenta", size=24, weight="bold"),
                        Divider(height=20, color="gray"),
                        username,
                        nombres,
                        apellidos,
                        Divider(height=20, color="gray"),
                        Text("Cambiar Contraseña", size=20, weight="bold"),
                        old_password,
                        new_password,
                        confirm_password,
                        ElevatedButton("Guardar Cambios", on_click=save_changes, bgcolor="blue", color="white"),
                    ],
                    spacing=20,
                    alignment="center",
                    horizontal_alignment="center",
                ),
            ],
            vertical_alignment="center",
            horizontal_alignment="center",
        )
    )
    page.dialog = message_dialog
    page.update()


