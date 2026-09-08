import cv2


JANELA_ORIGINAL = "Original"
JANELA_CINZA = "Escala de cinza"
JANELA_THRESHOLD = "Threshold"
JANELA_CONTROLE = "Controle"

NOME_TRACKBAR = "Threshold"

VALOR_INICIAL_THRESHOLD = 127
VALOR_MINIMO_THRESHOLD = 0
VALOR_MAXIMO_THRESHOLD = 255


def exibir_frame_original(frame):
    """Exibe o frame original."""
    cv2.imshow(JANELA_ORIGINAL, frame)


def exibir_frame_cinza(frame):
    """Exibe o frame em escala de cinza."""
    cv2.imshow(JANELA_CINZA, frame)


def exibir_frame_threshold(frame):
    """Exibe o frame após a aplicação do threshold."""
    cv2.imshow(JANELA_THRESHOLD, frame)


def criar_controle_threshold():
    """Cria a janela e a trackbar do threshold."""
    cv2.namedWindow(JANELA_CONTROLE)

    cv2.createTrackbar(
        NOME_TRACKBAR,
        JANELA_CONTROLE,
        VALOR_INICIAL_THRESHOLD,
        VALOR_MAXIMO_THRESHOLD,
        lambda valor: None,
    )


def obter_threshold():
    """Retorna o valor atual do threshold."""
    return cv2.getTrackbarPos(
        NOME_TRACKBAR,
        JANELA_CONTROLE
    )


def obter_tecla():
    """Obtém a tecla pressionada pelo usuário."""
    return cv2.waitKey(1) & 0xFF


def janela_foi_fechada():
    """Verifica se alguma janela da aplicação foi fechada."""
    janelas = [
        JANELA_ORIGINAL,
        JANELA_CINZA,
        JANELA_THRESHOLD,
        JANELA_CONTROLE,
    ]

    for janela in janelas:
        if cv2.getWindowProperty(
            janela,
            cv2.WND_PROP_VISIBLE
        ) < 1:
            return True

    return False


def deve_encerrar(tecla):
    """Verifica se o usuário solicitou o encerramento."""
    return tecla == ord("q") or janela_foi_fechada()


def fechar_interface():
    """Fecha todas as janelas da aplicação."""
    cv2.destroyAllWindows()