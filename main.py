from flet import app, Page
from views.login_view import show_login_view

def main(page: Page):
    page.title = "Money Transfer App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = 400
    page.window_height = 600
    
    # Cargar la primera vista (inicio de sesión)
    show_login_view(page)

# Inicia la aplicación
app(target=main)

