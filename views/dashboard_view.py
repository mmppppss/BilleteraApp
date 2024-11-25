from flet import View, Text, Column, ElevatedButton, Row, Divider

def show_dashboard_view(page):
    def transfer_clicked(e):
        print("Navegar a Transferir Dinero")

    def receive_clicked(e):
        print("Navegar a Recibir Dinero")

    def withdraw_clicked(e):
        print("Navegar a Retirar a Banco")

    def deposit_clicked(e):
        print("Navegar a Depositar desde Banco")

    def history_clicked(e):
        print("Navegar a Historial")

    def settings_clicked(e):
        print("Navegar a Configuración")

    # Simular saldo actual (esto se debería cargar desde la base de datos)
    current_balance = 1500.00  # Ejemplo de saldo
    balance_text = Text(f"Saldo actual: ${current_balance:,.2f}", size=36, weight="bold", color="green")

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

