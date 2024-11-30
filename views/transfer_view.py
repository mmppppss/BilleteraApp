from flet import View, Text, Column, TextField, Dropdown, ElevatedButton, Row, Divider, dropdown, AlertDialog
from views.utils import show_message, show_error
from database import searchUsers, getWalletUsuario
def show_transferir_view(page):

    def realizar_busqueda(e):

        # Simulación de resultados (puedes conectar esto a una base de datos)
        users = searchUsers(usuario_id_field.value)
        if users:
            print(users)
            user_options = [
                dropdown.Option(key=str(user["id"]), text=f"{user['username']} ({user['nombre']} {user['apellidos']})")
                for user in users
            ]
            user_dropdown = Dropdown(
                label="Seleccionar Usuario",
                options=user_options,
                width=400,
            )

            modal.controls = [user_dropdown]
            modal.open = True
            page.update()


    def seleccionar_usuario(user_id):
        usuario_id_field.value = user_id
        modal.open = False
        page.update()

    def confirmar_transferencia(e):
        usuario_id = usuario_id_field.value
        monto = monto_field.value
        if usuario_id and monto:
            show_error(page, f"Transfiriendo {monto} al usuario {usuario_id}")
        else:
            show_message(page, "Complete todos los campos antes de confirmar la transferencia")

    usuario_id_field = TextField(label="ID o nombre del usuario destino", width=300)
    buscar_button = ElevatedButton("Buscar usuario", on_click=realizar_busqueda)
    monto_field = TextField(label="Monto a transferir", width=300)
    confirmar_button = ElevatedButton("Confirmar transferencia", on_click=confirmar_transferencia)

    modal = AlertDialog(title=Text("Buscar Usuario"), open=False)

    page.views.clear()
    page.views.append(
        View(
            "/transferir",
            controls=[
                Column(
                    [
                        Text("Transferir Dinero", size=24, weight="bold"),
                        Divider(height=20, color="gray"),
                        Row([usuario_id_field, buscar_button], alignment="center", spacing=10),
                        monto_field,
                        Divider(height=20, color="transparent"),
                        confirmar_button,
                    ],
                    spacing=20,
                    alignment="center",
                    horizontal_alignment="center",
                )
            ],
            vertical_alignment="center",
            horizontal_alignment="center",
        )
    )
    page.dialog = modal
    page.update()

