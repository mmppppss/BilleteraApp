
import cv2
import flet as ft

# Función para detectar y devolver el valor del QR escaneado
def escanear_qr_con_camara():
    cap = cv2.VideoCapture(0)  # Abre la cámara (0 es la predeterminada)

    while True:
        ret, frame = cap.read()
        if not ret:
            return None

        # Detectar y decodificar QR
        detector = cv2.QRCodeDetector()
        value, pts, qr_code = detector.detectAndDecode(frame)  # Método correcto

        if value:
            cap.release()
            cv2.destroyAllWindows()
            return value

        # Mostrar el cuadro en tiempo real
        cv2.imshow("Escanear QR", frame)

        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

def main(page):
    def iniciar_escaneo(e):
        # Llamar a la función de escaneo y mostrar el resultado
        qr_result = escanear_qr_con_camara()
        if qr_result:
            page.add(ft.Text(f"Código QR escaneado: {qr_result}"))
        else:
            page.add(ft.Text("No se detectó ningún código QR."))

    # Interfaz de usuario
    page.add(
        ft.Column(
            [
                ft.ElevatedButton("Escanear QR", on_click=iniciar_escaneo),
                ft.Text("Presiona el botón para escanear un código QR desde la cámara."),
            ]
        )
    )

# Ejecutar la app de Flet
ft.app(target=main)

