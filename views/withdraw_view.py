from flet import View, Text, Column, ElevatedButton, TextField, Row, AlertDialog
from views.utils import show_message
from database import retirarDinero
from random import randint

def show_withdraw_view(page, wallet):
    def volver_clicked(e):
        from views.dashboard_view import show_dashboard_view
        show_dashboard_view(page, wallet["id_user"])

    def submit_withdraw(e):
        amount = withdraw_amount_field.value

        if not amount.isdigit() or float(amount) <= 0:
            show_message(page, "Por favor, ingrese un monto válido.")
            return

        amount = float(amount)
        
        if amount > wallet["amount"]:
            show_message(page, "Saldo insuficiente para realizar el retiro.")
        else:
            if retirarDinero(wallet["id_wallet"], amount, "Banco", randint(10000,99999)):
                show_message(page, f"Retiro de {wallet["money_abbreviation"]}.{amount:,.2f} exitoso.")
            else:
                show_message(page, "Error al realizar el retiro, por favor intente nuevamente.")

    withdraw_amount_field = TextField(label="Monto a Retirar", keyboard_type="number")

    submit_button = ElevatedButton("Retirar", on_click=submit_withdraw)

    volver_button = ElevatedButton("Volver", on_click=volver_clicked)

    page.views.clear()
    page.views.append(
        View(
            "/withdraw",
            controls=[
                Column(
                    [
                        Text(f"Retiro de dinero (simulado) desde tu billetera", size=24, weight="bold"),
                        withdraw_amount_field,
                        submit_button,
                        volver_button
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
