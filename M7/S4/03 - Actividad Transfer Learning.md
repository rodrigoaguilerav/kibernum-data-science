### 1. ¿Qué es data augmentation?

Es una técnica para **aumentar artificialmente** el tamaño y la diversidad del dataset modificando las imágenes originales con transformaciones aleatorias (rotaciones, recortes, flips, cambios de brillo, zoom, etc.), sin cambiar su etiqueta.
Ayuda a que el modelo **generalice mejor** y no se sobreajuste a las pocas imágenes disponibles.

---

### 2. ¿Por qué se reescalaron los píxeles en el preprocesamiento?

En el notebook se hace:

```python
image = tf.cast(image, tf.float32) / 255.0
```

Motivos:

- Pasar de enteros `[0, 255]` a flotantes `[0, 1]` mejora la **estabilidad numérica**.
- Muchos modelos preentrenados **suponen** que la entrada está normalizada.
- Facilita la **convergencia** del entrenamiento (gradientes más estables, learning rate más razonable).

---

### 3. ¿En qué consiste el freeze y unfreeze de las capas del modelo?

- **Freeze (congelar)**: `pretrained_model.trainable = False`
  - Los pesos de esas capas **no se actualizan** durante el entrenamiento.
  - Se usan solo como **extractor de características fijo**.
- **Unfreeze (descongelar)**:
  - Se marcan ciertas capas (normalmente las últimas) como `trainable = True`.
  - Se permite que sus pesos se **ajusten** a los datos específicos del nuevo problema.

En el ejemplo, inicialmente se deja el modelo preentrenado congelado para entrenar solo la “cabeza” nueva.

---

### 4. ¿En qué consiste la estrategia de entrenar un modelo base y después hacer fine tuning?

1. **Fase 1 – Modelo base congelado**:

   - Se toma el modelo preentrenado (`MobileNetV2` sin la parte de clasificación).
   - Se congela (`trainable = False`).
   - Se entrena solo la parte nueva (capas densas finales) sobre el dataset de flores.
   - Objetivo: adaptar rápidamente el clasificador final.
2. **Fase 2 – Fine tuning** (opcional, no siempre implementado):

   - Se descongelan algunas capas superiores del modelo base.
   - Se sigue entrenando con un **learning rate pequeño**.
   - Objetivo: ajustar finamente las representaciones del modelo preentrenado al nuevo dominio sin destruir lo ya aprendido.

---

### 5. ¿Por qué no se utilizó una capa softmax al agregar la capa de cabecera en el modelo base?

En el ejemplo:

- El **modelo base** (`pretrained_model`) se carga con `include_top=False`, es decir, **sin** su softmax original de ImageNet.
- La **nueva cabeza** que se añade sí termina en una capa:
  ```python
  tf.keras.layers.Dense(len(CLASSES), activation='softmax')
  ```
- No se aplica softmax **antes** (en el modelo base) porque:
  - El base debe producir **características continuas** ricas (mapas de activación).
  - Aplicar softmax en medio “aplastaría” esa información a una distribución de probabilidades y **perdería capacidad de representación**.
  - El softmax debe estar solo en la **última capa** de clasificación.

---

### 6. Conclusiones

- El notebook muestra un flujo típico de **transfer learning**:dataset pequeño → modelo simple (baseline) → modelo preentrenado congelado + cabeza nueva → entrenamiento y evaluación.
- El **reescalado** de píxeles y el uso de **pipelines `tf.data`** son claves para entrenar de forma estable y eficiente.
- Congelar y, si se quiere, luego descongelar capas permite **aprovechar conocimiento previo** (ImageNet) con pocos datos y poco cómputo.
- La arquitectura final (modelo base sin top + pooling + densas + softmax) ilustra bien cómo **separar extractor de características y clasificador** en transfer learning.

---

1. **Data augmentation**  
   Técnica para generar más datos a partir de los existentes aplicando transformaciones aleatorias (rotar, voltear, recortar, cambiar brillo, etc.), para reducir overfitting y mejorar generalización.

2. **Reescalado de píxeles**  
   Pasar de `[0,255]` a `[0,1]`:
   - estabiliza los cálculos (gradientes más suaves),
   - acelera y facilita el entrenamiento,
   - se ajusta a lo esperado por muchos modelos preentrenados.

3. **Freeze / unfreeze de capas**  
   - *Freeze*: `trainable = False` → las capas no actualizan sus pesos; actúan como extractor fijo.  
   - *Unfreeze*: `trainable = True` en algunas capas → se vuelven a entrenar para adaptarlas mejor al nuevo problema.

4. **Estrategia base + fine tuning**  
   - Primero se entrena solo la “cabeza” nueva con el modelo base congelado.  
   - Luego (opcional) se descongelan algunas capas del modelo base y se sigue entrenando con learning rate bajo para ajustar finamente.

5. **Softmax solo en la última capa**  
   - El modelo base (MobileNetV2) produce características continuas; no debe tener softmax.  
   - El softmax solo se aplica en la capa final de clasificación (la cabeza nueva con 5 neuronas).

6. **Conclusiones**  
   - Transfer learning permite buenos resultados con pocos datos.  
   - Normalización y buen pipeline de datos son esenciales.  
   - Congelar/descongelar capas controla cuánto del conocimiento previo se reutiliza y cuánto se ajusta al nuevo conjunto de flores.