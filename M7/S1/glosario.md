Un perceptrón es el modelo más simple de neurona artificial y la base histórica de las redes neuronales.

## ¿Qué es un perceptrón?

Es un modelo matemático que:

1. **Recibe entradas**  
   Un vector de características x = (x1, x2, ..., xn).

2. **Pondera las entradas**  
   Tiene pesos w = (w1, w2, ..., wn) y un sesgo b.  
   Calcula una suma ponderada:  
   z = w1·x1 + ... + wn·xn + b

3. **Aplica una función de activación**  
   En el perceptrón clásico es una función escalón:  
   y^ = 1 si z ≥ 0  
   y^ = 0 si z < 0

4. **Aprende los pesos**  
   Ajusta \(w\) y \(b\) iterativamente con una regla de aprendizaje (muy parecida a descenso de gradiente) para reducir los errores de clasificación.

Limitación importante: solo puede resolver problemas **linealmente separables** (separables por una recta / hiperplano).

---

## ¿Qué deberías saber de redes neuronales?

Piensa en una red neuronal como muchos perceptrones (neuronas) conectados en capas.

### 1. Arquitectura básica

- **Capas**:
  - Capa de entrada (features).
  - Una o más **capas ocultas**.
  - Capa de salida (clases, valores continuos, etc.).
- Cada neurona de una capa se conecta con varias de la siguiente capa.

### 2. Funciones de activación

Reemplazan el escalón por funciones suaves y diferenciables:

- ReLU, Leaky ReLU
- Sigmoid
- Tanh
- Softmax (para clasificación multiclase)

Son clave para que la red aprenda relaciones **no lineales**.

### 3. Aprendizaje: backpropagation + descenso de gradiente

- Se define una **función de pérdida**:
  - Clasificación: cross-entropy.
  - Regresión: MSE.
- Se hace:
  1. **Forward pass**: se calcula la predicción.
  2. **Backward pass (backpropagation)**: se calculan gradientes de la pérdida respecto a cada peso.
  3. **Actualización de pesos** con un optimizador (SGD, Adam, etc.).

### 4. Conceptos clave a manejar

- **Overfitting / underfitting** y cómo mitigarlos:
  - Regularización (L2, dropout, early stopping).
- **Hiperparámetros**:
  - Número de capas y neuronas.
  - Learning rate.
  - Número de épocas (epochs), batch size.
- **Preprocesamiento**:
  - Normalización/escalado de datos.
  - Codificación de variables categóricas (one-hot).
- **Tipos de redes**:
  - MLP (perceptrón multicapa) – la base.
  - CNN (Convolucionales) – imágenes.
  - RNN/LSTM/GRU – secuencias, texto, series de tiempo.