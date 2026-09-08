import cv2


def converter_para_cinza(frame):
    """Converte um frame colorido para escala de cinza."""
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def aplicar_threshold(frame_cinza, threshold):
    """Aplica threshold binário à imagem em escala de cinza."""
    _, frame_threshold = cv2.threshold(
        frame_cinza,
        threshold,
        255,
        cv2.THRESH_BINARY,
    )

    return frame_threshold


def calcular_histograma(frame_cinza):
    """Calcula o histograma da imagem em escala de cinza."""
    histograma = cv2.calcHist(
        [frame_cinza],
        [0],
        None,
        [256],
        [0, 256],
    )

    return histograma