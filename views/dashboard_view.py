from flet import View, Text, Column, ElevatedButton, Row, Divider
from database import getWalletUsuario 
from views.transfer_view import show_transferir_view
from views.recibir_view import show_recibir_view
from views.history_view import show_historial_view
from views.config_view import show_config_view
from views.withdraw_view import show_withdraw_view
from views.deposit_view import show_deposit_view
def show_dashboard_view(page, id):
    wallet = getWalletUsuario(id)
    print(wallet)
    def transfer_clicked(e):
        show_transferir_view(page, wallet)

    def receive_clicked(e):
        show_recibir_view(page, wallet)

    def withdraw_clicked(e):
        show_withdraw_view(page, wallet)

    def deposit_clicked(e):
        show_deposit_view(page, wallet)

    def history_clicked(e):
        show_historial_view(page, wallet)

    def settings_clicked(e):
        show_config_view(page, wallet)

    def login_clicked(e):
        from views.login_view import show_login_view  # Importación dentro de la función
        show_login_view(page)
    
    bienvenido_text = Text(f"No deberias ver esto, no hay sesion", size=24, weight="bold")
    current_balance = 0  # Ejemplo de saldo
    balance_text = Text(f"Saldo actual: ${current_balance:,.2f}", size=36, weight="bold", color="green")
    if wallet:
        bienvenido_text = Text(f"Bienvenido, {wallet['nombre']}", size=24, weight="bold")
        current_balance = wallet["amount"]
        balance_text = Text(f"Saldo actual: {wallet['money_abbreviation']}. {current_balance:,.2f}", size=36, weight="bold", color="green")


    # Crear los botones
    row1 = Row(
        controls=[
            ElevatedButton("Transferir", on_click=transfer_clicked),
            ElevatedButton("Recibir", on_click=receive_clicked),
        ],
        spacing=10,
        alignment="center",
    )

    row2 = Row(
        controls=[
            ElevatedButton("Retirar a Banco", on_click=withdraw_clicked),
            ElevatedButton("Depositar desde Banco", on_click=deposit_clicked),
        ],
        spacing=10,
        alignment="center",
    )

    row3 = Row(
        controls=[
            ElevatedButton("Historial", on_click=history_clicked),
            ElevatedButton("Configuración", on_click=settings_clicked),  # Función adicional sugerida
        ],
        spacing=10,
        alignment="center",
    )

    # Crear la vista
    page.views.clear()
    page.views.append(
        View(
            "/dashboard",
            controls=[
                Column(
                    [
                        bienvenido_text,
                        balance_text,
                        Divider(height=20, color="gray"),
                        row1,
                        Divider(height=10, color="transparent"),
                        row2,
                        Divider(height=10, color="transparent"),
                        row3,
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

