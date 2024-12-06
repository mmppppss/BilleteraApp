from flet import (
    View,
    Text,
    Column,
    TextField,
    Dropdown,
    ElevatedButton,
    Row,
    Divider,
    dropdown,
    AlertDialog,
    IconButton,
    icons,
    Page,
)
from views.utils import show_message, show_error
from database import searchUsers, transferirDinero

def show_transferir_view(page: Page, wallet):

    def volver_clicked(e):
        from views.dashboard_view import show_dashboard_view
        show_dashboard_view(page, wallet["id_user"]);
    # Campo de búsqueda y monto
    usuario_id_field = TextField(label="ID o nombre del usuario destino", width=300)
    monto_field = TextField(label="Monto a transferir", width=300)

    # Diálogo de búsqueda
    dialog_search_field = TextField(label="Buscar usuario")
    dialog_dropdown = Dropdown(label="Resultados de búsqueda", width=400, options=[])
    buscar_dialog_button = ElevatedButton("Buscar", on_click=None)
    seleccionar_button = ElevatedButton("Seleccionar", on_click=None)
    volver_button = ElevatedButton("Volver", on_click=volver_clicked)
    modal = AlertDialog(
        title=Text("Buscar Usuario"),
        content=Column(
            [
                dialog_search_field,
                buscar_dialog_button,
                dialog_dropdown,
                Divider(height=10, color="transparent"),
                seleccionar_button,
            ],
            spacing=2,
            width=400,
            height=400,
            alignment="center",
            horizontal_alignment="center",
        ),
        actions=[],
        open=False,
    )

    def abrir_dialogo(e):
        modal.open = True
        page.dialog = modal
        page.update()

    def realizar_busqueda(e):
        strBusqueda = dialog_search_field.value
        users = searchUsers(strBusqueda)
        if users:
            user_options = [
                dropdown.Option(key=str(user["id"]), text=f"{user['username']} ({user['nombre']} {user['apellidos']})")
                for user in users
            ]
            dialog_dropdown.options = user_options
            dialog_dropdown.value = None  # Restablecer selección
            dialog_dropdown.update()
        else:
            show_message(page, "No se encontraron usuarios similares")

    def seleccionar_usuario(e):
        if dialog_dropdown.value:
            usuario_id_field.value = dialog_dropdown.value
            modal.open = False
            page.update()

    # Vincular botones del cuadro de diálogo
    buscar_dialog_button.on_click = realizar_busqueda
    seleccionar_button.on_click = seleccionar_usuario

    # Confirmación de transferencia
    def confirmar_transferencia(e):
        userToId = usuario_id_field.value
        monto = monto_field.value
        if userToId and monto:
            show_message(page, f"Transfiriendo {monto} al usuario")
            if transferirDinero(wallet["id_wallet"], userToId, monto):
                show_message(page, f"Transferencia exitosa")
        else:
            show_message(page, "Complete todos los campos antes de confirmar la transferencia")

    # Botón de búsqueda en la vista principal
    buscar_button = IconButton(icon=icons.SEARCH, on_click=abrir_dialogo)
    confirmar_button = ElevatedButton("Confirmar transferencia", on_click=confirmar_transferencia)

    # Vista principal
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
                        volver_button,
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
    page.update()

