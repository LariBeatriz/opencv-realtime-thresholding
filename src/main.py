from webcam import (
    encontrar_webcams_linux,
    abrir_webcam,
    capturar_frame,
    liberar_webcam,
)

from processamento import (
    converter_para_cinza,
    aplicar_threshold,
    calcular_histograma,
)

from interface import (
    exibir_frame_original,
    exibir_frame_cinza,
    exibir_frame_threshold,
    exibir_histograma,
    criar_controle_threshold,
    obter_threshold,
    obter_tecla,
    deve_encerrar,
    fechar_interface,
)


def main():
    dispositivos = encontrar_webcams_linux()

    if not dispositivos:
        print("Nenhuma webcam encontrada.")
        return

    dispositivo = dispositivos[0]

    print(f"Webcam encontrada: {dispositivo}")

    camera = abrir_webcam(dispositivo)

    criar_controle_threshold()

    try:
        while True:
            frame = capturar_frame(camera)

            frame_cinza = converter_para_cinza(frame)

            histograma = calcular_histograma(frame_cinza)

            threshold = obter_threshold()

            frame_threshold = aplicar_threshold(
                frame_cinza,
                threshold,
            )

            exibir_frame_original(frame)
            exibir_frame_cinza(frame_cinza)
            exibir_frame_threshold(frame_threshold)
            exibir_histograma(histograma)
            tecla = obter_tecla()

            if deve_encerrar(tecla):
                break

    finally:
        liberar_webcam(camera)
        fechar_interface()


if __name__ == "__main__":
    main()