from flet import(
        View, Column, Text, DataTable,
        DataColumn, DataRow, DataCell,
        Divider, ElevatedButton, AlertDialog
    )
from database import obtener_transferencias

def show_historial_view(page, wallet):
    transfer_history = obtener_transferencias(wallet["id_wallet"])

    detail_dialog = AlertDialog()

    def volver_clicked(e):
        from views.dashboard_view import show_dashboard_view
        show_dashboard_view(page, wallet["id_user"])
    
    def show_detail(log):
        def close_detail_dialog(e):
            page.dialog.open = False
            page.update()

        page.dialog= AlertDialog(
            title=Text("Detalles de transaccion"),
            content=Column(
                [
                    Text(f"ID Log: {log['id_log']}", size=16),
                    Text(f"Fecha: {log['date']}", size=16),
                    Text(f"Hora: {log['hour']}", size=16),
                    Text(f"Wallet Origen: {log['id_wallet_from']}", size=16),
                    Text(f"Wallet Destino: {log['id_wallet_to']}", size=16),
                    Text(f"Monto: ${log['amount']:.2f}", size=16),
                    Text(f"Usuario Destino: {log['username_to']}", size=16),
                    Text(f"IPv4: {log['ipv4']}", size=16),
                    Text(f"Navegador: {log['browser']}", size=16),
                ],
            ),
            actions=[
                ElevatedButton("OK", on_click=close_detail_dialog),
            ]
        )
        page.dialog.open = True;
        page.update()
    rows = [
        DataRow(
            cells=[
                #DataCell(Text(str(log["id_log"]))),
                DataCell(Text(log["date"])),
                DataCell(Text(log["hour"])),
                #DataCell(Text(str(log["id_wallet_from"]))),
                DataCell(Text(str(log["id_wallet_to"]))),
                DataCell(Text(f"${log['amount']:.2f}")),
                DataCell(Text(log["username_to"])),  
                #DataCell(Text(log["ipv4"])),
                #DataCell(Text(log["browser"])),
                DataCell(
                    ElevatedButton(
                        "Detalles",
                        on_click=lambda e, log=log: show_detail(log),
                        bgcolor="blue",
                        color="white",
                    )
                ),
            ]
        )
        for log in transfer_history
    ]

    # Crear la vista
    page.views.clear()
    page.views.append(
        View(
            "/historial",
            controls=[
                Column(
                    [
                        Text("Historial de Transferencias", size=24, weight="bold"),
                        Divider(height=20, color="gray"),
                        DataTable(
                            columns=[
                                #DataColumn(Text("ID Log")),
                                DataColumn(Text("Fecha")),
                                DataColumn(Text("Hora")),
                                #DataColumn(Text("Wallet Origen")),
                                DataColumn(Text("Billetera Destino")),
                                DataColumn(Text("Monto")),
                                DataColumn(Text("Usuario Destino")),  # Nueva columna
                                #DataColumn(Text("IPv4")),
                                #DataColumn(Text("Navegador")),
                                DataColumn(Text("Detalles")),
                            ],
                            rows=rows,
                            width=1000,
                        ),
                    ],
                    spacing=20,
                    alignment="center",
                    horizontal_alignment="center",
                ),
                ElevatedButton("Volver", on_click=volver_clicked),
            ],
            vertical_alignment="center",
            horizontal_alignment="center",
        )
    )
    page.update()

