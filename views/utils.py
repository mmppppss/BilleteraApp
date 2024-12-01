from flet import ElevatedButton, Page, Text,SnackBar, AlertDialog

def show_message(page, message):
    page.snack_bar = SnackBar(content=Text(message))
    page.snack_bar.open = True
    page.update()

def show_error(page, message):

    def close_dialog(e):
        page.dialog.open = False
        page.update()
    page.dialog = AlertDialog(
        title=Text("Error"),
        content=Text(message),
        actions=[
            ElevatedButton("Cerrar", on_click=close_dialog)
        ],
    )
    page.dialog.open = True
    page.update()

