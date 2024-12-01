from flet import View, Text, Column, ElevatedButton, Divider, Image
import qrcode
import io
import base64


def show_recibir_view(page, user_info):
    qr_data = {
        "username": user_info["username"],
        "id": user_info["id_user"],
        "id_wallet": user_info["id_wallet"]}
    qr = qrcode.QRCode()
    qr.add_data(qr_data)
    qr.make(fit=True)

    qr_img = io.BytesIO()
    qr_img_data = qr.make_image(fill="black", back_color="white")
    qr_img_data.save(qr_img)  
    qr_img.seek(0)

    qr_base64 = base64.b64encode(qr_img.getvalue()).decode("utf-8")
    qr_code_image = Image(src_base64=qr_base64, width=200, height=200)

    user_text = Text(f"Usuario: {user_info['username']}", size=16, weight="bold")
    def volver_clicked(e):
        from views.dashboard_view import show_dashboard_view
        show_dashboard_view(page, user_info["id_user"]);

    volver_button = ElevatedButton("Volver", on_click=volver_clicked)
    page.views.clear()
    page.views.append(
        View(
            "/recibir",
            controls=[
                Column(
                    [
                        Text("Recibir Dinero", size=24, weight="bold"),
                        Divider(height=20, color="gray"),
                        user_text,
                        Divider(height=20, color="transparent"),
                        qr_code_image,
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

