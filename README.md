# 👁️ Real-Time Threshold Explorer com OpenCV

Aplicação desenvolvida em Python e OpenCV para demonstrar na prática o conceito de **Thresholding (Limiarização)** e manipulação de pixels em tempo real através da webcam.

Atividade acadêmica: **U1A1 - Entendendo o uso de Threshold**.

---

## 🎯 Funcionalidades

- **Captura em Tempo Real:** Leitura de vídeo direto da webcam.
- **Conversão de Cores:** Transformação dos frames RGB para escala de cinza (*grayscale*).
- **Ajuste Dinâmico (Trackbar):** Controle do valor de corte do threshold (0 a 255) em tempo de execução.
- **Visualização Simultânea:**
  - Imagem Original (Colorida)
  - Escala de Cinza
  - Imagem Binarizada (Threshold aplicado)
- *(Opcional)* Análise de distribuição de intensidade via **Histograma**.

---

## 🧠 Conceitos Abordados

* **Pixel & Intensidade:** Representação digital da imagem onde cada pixel em escala de cinza varia entre `0` (preto) e `255` (branco).
* **Thresholding Binário:** Transformação matemática onde pixels com intensidade acima do limite definido tornam-se brancos (`255`) e os demais tornam-se pretos (`0`).
* **Impacto da Iluminação:** Variação dos valores de luminância do ambiente e a não existência de um limiar universalmente ideal sem controle de iluminação.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x
- Bibliotecas necessárias:

```bash
pip install opencv-python numpy matplotlib
