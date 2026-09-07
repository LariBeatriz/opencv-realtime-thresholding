import cv2
from pathlib import Path


def encontrar_webcams_linux():
    dispositivos = sorted(Path("/dev").glob("video*"))

    return dispositivos


def abrir_webcam(dispositivo):
    camera = cv2.VideoCapture(str(dispositivo), cv2.CAP_V4L2)

    if not camera.isOpened():
        camera.release()
        raise RuntimeError(
            f"Não foi possível abrir a webcam: {dispositivo}"
        )

    return camera


def capturar_frame(camera):
    sucesso, frame = camera.read()

    if not sucesso:
        raise RuntimeError(
            "Não foi possível capturar um frame da webcam."
        )

    return frame


def liberar_webcam(camera):
    camera.release()
    cv2.destroyAllWindows()