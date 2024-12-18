from flet import (
    Text,
    TextField,
    ElevatedButton,
    View,
    Column,
    Row,
    Divider,
    Page,
)
from database import update_password

# Función para mostrar la vista de perfil
def show_config_view(page, user_info):
    # Campo de mensaje para notificaciones
    message_text = Text("", color="red")

    def save_changes(e):
        # Validar contraseñas
        if new_password_field.value != confirm_password_field.value:
            message_text.value = "Las contraseñas no coinciden."
            message_text.color = "red"
            page.update()
            return
        
        print("Guardando cambios...")
        print(f"Contraseña actual: {current_password_field.value}")
        print(f"Nueva contraseña: {new_password_field.value}")
        update_password( user_info["id_user"], current_password_field.value, new_password_field.value);
        # Feedback al usuario
        message_text.value = "¡Perfil actualizado con éxito!"
        message_text.color = "green"
        page.update()

    def cancel_changes(e):
        # Regresar a la página principal o vista anterior
        from views.dashboard_view import show_dashboard_view
        show_dashboard_view(page, user_info["id_user"])

    # Crear campos del formulario
    current_password_field = TextField(label="Contraseña actual", password=True, width=400)
    new_password_field = TextField(label="Nueva contraseña", password=True, width=400)
    confirm_password_field = TextField(label="Confirmar nueva contraseña", password=True, width=400)

    # Botones de acción
    save_button = ElevatedButton("Guardar cambios", on_click=save_changes)
    cancel_button = ElevatedButton("Cancelar", on_click=cancel_changes)

    # Agregar los elementos a la vista
    page.views.clear()
    page.views.append(
        View(
            "/profile",
            controls=[
                Column(
                    [
                        Text("Editar perfil", size=24, weight="bold"),
                        Divider(height=10, color="transparent"),
                        current_password_field,
                        new_password_field,
                        confirm_password_field,
                        Divider(height=10),
                        message_text,  # Mensaje de notificación
                        Divider(height=20),
                        Row([save_button, cancel_button], alignment="center", spacing=20),
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

# Ejecutar app
if __name__ == "__main__":
    import flet as ft
    ft.app(target=main)
