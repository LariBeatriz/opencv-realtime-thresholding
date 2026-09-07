import cv2

from webcam import (
    encontrar_webcams_linux,
    abrir_webcam,
    capturar_frame,
    liberar_webcam,
)


def main():
    dispositivos = encontrar_webcams_linux()

    if not dispositivos:
        print("Nenhuma webcam encontrada.")
        return

    dispositivo = dispositivos[0]

    print(f"Webcam encontrada: {dispositivo}")

    camera = abrir_webcam(dispositivo)

    try:
        while True:
            frame = capturar_frame(camera)

            cv2.imshow("Webcam", frame)

            tecla = cv2.waitKey(1) & 0xFF

            if tecla == ord("q"):
                break

    finally:
        liberar_webcam(camera)


if __name__ == "__main__":
    main()