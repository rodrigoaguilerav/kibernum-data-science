### CNN vs Fully Connected Network (FCN)

#### 1. ¿Qué es cada una?

- **FCN (red totalmente conectada / MLP)**  
  Red donde **cada neurona de una capa está conectada con todas** las neuronas de la capa siguiente.  
  Ejemplo típico: vectores de entrada tabulares, embeddings, etc.

- **CNN (Convolutional Neural Network)**  
  Red que usa **capas convolucionales** y **pooling** para procesar datos con estructura espacial (imágenes, audio, señales 2D/3D). Explota la estructura local.

---

#### 2. Características principales

**FCN:**
- Entrada normalmente como **vector 1D** (hay que “aplanar” la imagen).
- **Muchos parámetros** cuando la entrada es grande (por eso no escala bien a imágenes grandes).
- No aprovecha la **información espacial** (posición relativa de los píxeles).
- Suele usarse para:
  - Datos tabulares.
  - Capas finales de clasificación sobre features ya extraídas.

**CNN:**
- Trabaja con tensores tipo **(alto, ancho, canales)**.
- Usa:
  - **Convoluciones** → detectan patrones locales (bordes, texturas, formas).
  - **Pooling** → reduce tamaño y hace la red más robusta a traslaciones pequeñas.
- Comparte pesos (mismo filtro se aplica en toda la imagen) → **muchos menos parámetros** que una FCN equivalente.
- Suele usarse para:
  - Clasificación de imágenes.
  - Detección/segmentación de objetos.
  - Visión por computador en general.

---

#### 3. Datos importantes a tener en cuenta

- **Dimensión de entrada**  
  - Si tienes imágenes o datos con estructura espacial → **CNN** suele ser la mejor opción.  
  - Si son vectores/tablas sin estructura espacial clara → **FCN/MLP** es más natural.

- **Cantidad de parámetros y overfitting**
  - FCN con imágenes grandes → número de parámetros explota, alto riesgo de overfitting.
  - CNN controla mejor el número de parámetros gracias al **weight sharing** (mismos kernels en toda la imagen).

- **Interpretabilidad de features**
  - CNN aprende filtros interpretables: bordes, texturas, partes, etc.
  - FCN aprende relaciones globales en el vector, menos estructuradas espacialmente.

- **Costo computacional**
  - CNN está muy optimizada en GPUs y bibliotecas modernas.
  - FCN grande sobre imágenes planas suele ser ineficiente y peor en performance.