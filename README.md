# 👁️ Real-Time Threshold Explorer com OpenCV

Aplicação de processamento digital de imagens desenvolvida em Python e OpenCV para captura de vídeo em tempo real, conversão para escala de cinza, aplicação de threshold binário e análise da distribuição de intensidades por meio de histograma.

O projeto foi desenvolvido como atividade prática para compreender os conceitos fundamentais de **pixel, intensidade, escala de cinza, threshold, segmentação de imagens e histograma**.

---

## 📌 Sobre o projeto

O projeto utiliza uma webcam para capturar imagens em tempo real e processá-las utilizando técnicas básicas de visão computacional.

O fluxo de processamento é:

```text
Webcam
   ↓
Imagem original
   ↓
Escala de cinza
   ↓
Threshold binário
   ↓
Imagem binária
   ↓
Histograma
````

O valor do threshold pode ser ajustado em tempo real através de uma **trackbar**, permitindo observar imediatamente como diferentes valores alteram o resultado da segmentação.

---

## 🎯 Objetivos

* Capturar imagens utilizando uma webcam.
* Converter imagens coloridas para escala de cinza.
* Compreender a representação de intensidade dos pixels.
* Aplicar threshold binário.
* Ajustar o threshold em tempo real.
* Comparar diferentes valores de threshold.
* Analisar a influência da iluminação no resultado.
* Visualizar a distribuição de intensidades através de um histograma.
* Compreender as limitações de um threshold fixo.
* Aplicar conceitos básicos de processamento digital de imagens.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **OpenCV**
* **NumPy**
* **Webcam**

---

## 📂 Estrutura do projeto

```text
opencv-realtime-thresholding/
│
├── src/
│   ├── main.py
│   ├── webcam.py
│   ├── processamento.py
│   └── interface.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

### Responsabilidade dos módulos

#### `main.py`

Responsável pela **orquestração da aplicação**.

Coordena:

* captura dos frames;
* conversão para escala de cinza;
* cálculo do histograma;
* aplicação do threshold;
* atualização da interface;
* encerramento da aplicação.

A implementação das funcionalidades fica nos módulos especializados.

#### `webcam.py`

Responsável pelas operações relacionadas à webcam:

* localização dos dispositivos de vídeo;
* abertura da câmera;
* captura de frames;
* liberação do dispositivo.

#### `processamento.py`

Responsável pelo processamento das imagens:

* conversão para escala de cinza;
* aplicação do threshold;
* cálculo do histograma.

#### `interface.py`

Responsável pela interação visual:

* criação das janelas;
* criação da trackbar;
* exibição das imagens;
* exibição do histograma;
* leitura de teclas;
* detecção do fechamento das janelas.

---

# ⚙️ Como funciona

## 1. Captura da imagem

A webcam captura continuamente frames do ambiente.

Cada frame é representado como uma matriz de pixels.

Uma imagem colorida normalmente utiliza três canais:

```text
B → Blue
G → Green
R → Red
```

---

## 2. Conversão para escala de cinza

O frame colorido é convertido para uma imagem em escala de cinza.

Em vez de possuir três canais de cor, cada pixel passa a possuir uma única intensidade.

A intensidade varia entre:

```text
0   → preto
255 → branco
```

Valores intermediários representam diferentes tons de cinza.

A conversão é realizada utilizando:

```python
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

---

# 🔲 Threshold

O threshold transforma a imagem em escala de cinza em uma imagem binária.

O projeto utiliza:

```python
cv2.threshold(
    frame_cinza,
    threshold,
    255,
    cv2.THRESH_BINARY,
)
```

A regra utilizada é:

```text
Se intensidade > threshold:
    pixel = 255
Caso contrário:
    pixel = 0
```

Matematicamente:

```text
                 255, se G(x,y) > T
B(x,y) =
                   0, caso contrário
```

Onde:

* `G(x,y)` representa a intensidade do pixel;
* `T` representa o valor do threshold;
* `B(x,y)` representa o pixel resultante.

---

## 🎚️ Ajuste do threshold

O valor do threshold pode ser alterado através de uma trackbar.

O intervalo disponível é:

```text
0 ─────────────────────────────── 255
```

Isso permite observar o comportamento da segmentação em tempo real.

### Threshold baixo

Exemplo:

```text
T = 50
```

Mais pixels possuem intensidade superior a 50.

Consequentemente, uma quantidade maior de pixels tende a se tornar branca.

### Threshold intermediário

Exemplo:

```text
T = 127
```

O resultado tende a apresentar uma divisão mais equilibrada entre regiões claras e escuras, dependendo da imagem.

### Threshold alto

Exemplo:

```text
T = 200
```

Somente pixels com intensidade elevada ultrapassam o threshold.

Consequentemente, uma quantidade maior de pixels tende a se tornar preta.

---

# 📊 Histograma

O projeto também calcula o histograma da imagem em escala de cinza.

O histograma representa a quantidade de pixels existente em cada nível de intensidade.

```text
Eixo X → intensidade dos pixels (0–255)

Eixo Y → quantidade de pixels
```

O cálculo é realizado utilizando:

```python
cv2.calcHist(
    [frame_cinza],
    [0],
    None,
    [256],
    [0, 256],
)
```

O histograma permite analisar a distribuição dos níveis de cinza presentes na imagem.

Por exemplo:

* concentração próxima de `0` → predominância de regiões escuras;
* concentração próxima de `255` → predominância de regiões claras;
* distribuição ampla → presença de diferentes níveis de intensidade.

---

# 🔬 Relação entre histograma e threshold

O histograma ajuda a compreender o efeito da escolha do threshold.

Considere uma imagem com muitos pixels concentrados entre `80` e `180`.

Se:

```text
T = 50
```

grande parte desses pixels será classificada como branca.

Se:

```text
T = 200
```

esses mesmos pixels serão classificados como pretos.

Portanto, o threshold funciona como um **limiar de decisão sobre a distribuição de intensidades**.

Isso torna o histograma uma ferramenta útil para analisar e justificar escolhas de threshold.

---

# 💡 Influência da iluminação

A iluminação possui influência direta sobre o resultado.

A câmera não registra simplesmente "objetos claros" e "objetos escuros". Ela registra valores de intensidade que dependem das condições de captura.

Por exemplo, uma mesma superfície pode apresentar:

```text
Boa iluminação → intensidade ≈ 220
Pouca iluminação → intensidade ≈ 140
```

Considerando:

```text
Threshold = 200
```

teríamos:

```text
220 > 200 → branco
140 > 200 → preto
```

Portanto, a mesma região física pode ser classificada de maneiras diferentes dependendo da iluminação.

---

# 🧪 Experimentos

Durante os testes, devem ser observados pelo menos os seguintes valores:

| Threshold | Resultado observado | Interpretação |
| --------- | ------------------- | ------------- |
| 50        |                     |               |
| 127       |                     |               |
| 200       |                     |               |

Também é recomendado testar valores extremos:

```text
0
10
50
127
200
240
255
```

Além disso, recomenda-se realizar os testes sob diferentes condições de iluminação.

### Questões analisadas

* O que acontece quando o threshold é muito baixo?
* O que acontece quando o threshold é muito alto?
* Por que determinados detalhes desaparecem?
* Como a iluminação altera o resultado?
* Existe um threshold universalmente ideal?
* Como o histograma pode auxiliar na escolha do threshold?

---

# ▶️ Instalação

## Pré-requisitos

Antes de executar o projeto, é necessário possuir:

* Python 3.10 ou superior;
* Webcam funcional;

---

## 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd opencv-realtime-thresholding
code .
```

---

## 2. Crie um ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

No Windows:

```powershell
python -m venv .venv
```

Ative:

```powershell
.venv\Scripts\activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🚀 Execução

Com o ambiente virtual ativado, execute:

```bash
python src/main.py
```

A aplicação deverá abrir as seguintes janelas:

```text
┌─────────────────────┐
│       Original      │
└─────────────────────┘

┌─────────────────────┐
│   Escala de cinza   │
└─────────────────────┘

┌─────────────────────┐
│      Threshold      │
└─────────────────────┘

┌─────────────────────┐
│     Histograma      │
└─────────────────────┘

┌─────────────────────┐
│      Controle       │
│ Threshold ───●────  │
└─────────────────────┘
```

Movimente a trackbar para alterar o threshold em tempo real.

Para encerrar:

```text
Q
```

ou feche uma das janelas da aplicação.

---

# 🐧 Observação sobre Linux

No Linux, as webcams normalmente são disponibilizadas através de dispositivos como:

```text
/dev/video0
/dev/video1
/dev/video2
...
```

O projeto procura dispositivos de vídeo disponíveis em `/dev` em vez de depender exclusivamente de um índice fixo.

Isso reduz a dependência de uma configuração específica da máquina.

---

# 🧠 Conceitos abordados

Este projeto permite praticar conceitos fundamentais de visão computacional e processamento digital de imagens:

### Pixel

Unidade básica de uma imagem digital.

### Intensidade

Valor associado ao brilho de um pixel em uma imagem em escala de cinza.

Intervalo:

```text
0 → 255
```

### Escala de cinza

Representação em que cada pixel possui apenas um valor de intensidade.

### Threshold

Limiar utilizado para classificar pixels em diferentes grupos.

### Imagem binária

Imagem composta por dois valores:

```text
0   → preto
255 → branco
```

### Segmentação

Processo de separar regiões de uma imagem com base em determinadas características.

### Histograma

Representação da distribuição das intensidades dos pixels de uma imagem.

---

# 📈 Resultados esperados

Espera-se observar que:

* thresholds baixos produzem imagens predominantemente brancas;
* thresholds altos produzem imagens predominantemente pretas;
* diferentes objetos apresentam diferentes distribuições de intensidade;
* mudanças na iluminação alteram a distribuição dos pixels;
* detalhes podem desaparecer dependendo do threshold;
* um threshold fixo pode não funcionar adequadamente em todas as condições.

---

# ⚠️ Limitações

O método utilizado é simples e possui algumas limitações.

Um único threshold fixo pode apresentar resultados inadequados quando:

* a iluminação não é uniforme;
* existe forte variação de luminosidade;
* objeto e fundo possuem intensidades semelhantes;
* a câmera altera automaticamente exposição ou ganho;
* existem sombras na cena.

Em aplicações mais complexas, técnicas como **threshold adaptativo**, **Otsu**, normalização de iluminação e outros métodos de segmentação podem produzir resultados melhores.

---

# 👥 Autores

Projeto acadêmico desenvolvido por:

* **Larissa Beatriz**