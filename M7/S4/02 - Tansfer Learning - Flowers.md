flujo completo de **clasificación de flores** con deep learning:

1. Carga y exploración de datos.
2. Definición de “pipelines” de entrada.
3. Entrenamiento de:
   - Un modelo muy simple (baseline).
   - Un modelo con **transfer learning** usando MobileNetV2.
4. Evaluación y visualización de resultados.

---

## 1. Imports e información básica

- Importa librerías: `os`, `sys`, `math`, `numpy`, `matplotlib.pyplot`, `tensorflow`.
- Imprime la versión de TensorFlow.
- Define `AUTOTUNE` para optimizar el pipeline de datos con `tf.data`.

---

## 2. Configuración de parámetros (tamaño, clases, etc.)

Hay dos bloques de configuración (uno original de GCS y otro adaptado):

- Define constantes relacionadas con el dataset original de Google Cloud:
  - `GCS_PATTERN`, `GCS_OUTPUT`, `SHARDS`, `TARGET_SIZE`, `CLASSES` (bytes).
- Luego, en la sección de **Configuración**, redefine:
  - `EPOCHS = 12`.
  - `IMAGE_SIZE = [331, 331]`.
  - `FLOWERS_DATASETS`: rutas en GCS para distintos tamaños de imagen (192, 224, 331, 512).
  - `CLASSES` como lista de strings: `['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']`.
  - Aserciones para asegurar que la imagen es cuadrada y de un tamaño soportado.

---

## 3. Selección de dispositivo y estrategia de distribución

- Intenta conectarse a un **TPU**:
  - Si funciona: usa `tf.distribute.TPUStrategy`.
  - Si no: usa `tf.distribute.MirroredStrategy()` (para 1 o varias GPUs / CPU).
- Imprime el número de réplicas (`strategy.num_replicas_in_sync`).

Esto sirve para que el modelo se entrene de forma distribuida si hay varios dispositivos.

---

## 4. Configuración de batch size y learning rate schedule

En función del número de réplicas:

- Ajusta:
  - `BATCH_SIZE` y `VALIDATION_BATCH_SIZE`.
  - Parámetros del **learning rate**: `start_lr`, `max_lr`, `min_lr`, `rampup_epochs`, etc.
- Define una función `lrfn(epoch)` que devuelve el **learning rate** según la época:
  - Aumenta progresivamente (ramp-up).
  - Opcionalmente se mantiene (sustain).
  - Luego decrece exponencialmente (decay).
- Crea un callback `LearningRateScheduler` para usar `lrfn`.
- Grafica la curva del learning rate para inspeccionarla.

---

## 5. (Opcional) Mixed precision

- Define `MIXED_PRECISION = False`.
- Si estuviera en `True`, activaría políticas de precisión mixta (`mixed_bfloat16` o `mixed_float16`) y XLA para acelerar en TPU/GPU.

En este notebook se deja desactivado.

---

## 6. Funciones de visualización (display utilities)

Define varias funciones auxiliares para:

- Convertir un `dataset` de TensorFlow en arrays de NumPy (`dataset_to_numpy_util`).
- Crear títulos con la clase predicha vs la correcta (`title_from_label_and_target`).
- Mostrar una imagen individual (`display_one_flower`).
- Mostrar 9 imágenes aleatorias de un dataset (`display_9_images_from_dataset`).
- Mostrar 9 imágenes con sus **predicciones** y resaltar las incorrectas en rojo (`display_9_images_with_predictions`).
- Graficar curvas de entrenamiento/validación (`display_training_curves`).

Estas funciones se usan más adelante para inspeccionar resultados.

---

## 7. Lectura de imágenes desde TFRecords (versión GCS)

Se definen funciones para trabajar con archivos TFRecord (formato original del curso):

1. `read_tfrecord(example)`:
   - Define el esquema de las features (`image` como string, `class` como int64).
   - Decodifica la imagen JPEG.
   - Normaliza los píxeles a `[0, 1]`.
   - Redimensiona a `IMAGE_SIZE`.
   - Retorna `(image, class_label)`.

2. `load_dataset(filenames)`:
   - Crea un `TFRecordDataset` a partir de una lista de archivos `.tfrec`.
   - Desactiva el orden determinista para hacer el pipeline más rápido.
   - Mapea cada ejemplo con `read_tfrecord`.
   - Retorna un `tf.data.Dataset` de `(imagen, etiqueta)`.

Estas funciones se usan luego para:
- Crear datasets de entrenamiento/validación desde rutas GCS.
- Mostrar/usar imágenes en predicciones finales.

---

## 8. Descarga local del dataset con `tensorflow_datasets`

Para evitar problemas de permisos con GCS:

- Importa `tensorflow_datasets` (`tfds`).
- Descarga el dataset `"tf_flowers"` directamente con:
  - `split=['train[:80%]', 'train[80%:]']` → 80% train, 20% valid.
  - `as_supervised=True` → retorna `(imagen, etiqueta)`.
- Define `preprocess_image`:
  - Redimensiona la imagen a `[331, 331]`.
  - Normaliza píxeles a `[0, 1]`.
- Crea un dataset `dataset = ds_train.map(preprocess_image)`.
- Muestra 9 imágenes usando `display_9_images_from_dataset(dataset)` para explorar los datos.

---

## 9. Modelo simple (baseline) entrenado con datos locales

Bloque llamado “BLOQUE ÚNICO DE CARGA Y ENTRENAMIENTO”:

1. Vuelve a importar Keras (por claridad) y define:
   - `IMAGE_SIZE_LOCAL = [331, 331]`.
   - `BATCH_SIZE_LOCAL = 16`.

2. `preprocess_local` (similar a `preprocess_image`):
   - Redimensiona a 331x331.
   - Normaliza a `[0, 1]`.

3. Crea los datasets de entrenamiento y validación:
   - `train_ds`:
     - `map(preprocess_local)`
     - `cache()`
     - `shuffle(1000)`
     - `batch(BATCH_SIZE_LOCAL)`
     - `repeat()` (para poder iterar muchas épocas)
     - `prefetch(AUTOTUNE)`
   - `valid_ds`:
     - `map(preprocess_local)`
     - `batch(BATCH_SIZE_LOCAL)`
     - `cache()`
     - `prefetch(AUTOTUNE)`

4. Define un **modelo muy sencillo**:
   - `Sequential([ Flatten(input_shape=(331, 331, 3)), Dense(5, activation='softmax') ])`
   - Solo aplanado + una capa densa softmax (5 clases).

5. Compila el modelo:
   - `optimizer='adam'`
   - `loss='sparse_categorical_crossentropy'`
   - `metrics=['accuracy']`

6. Calcula `steps_per_epoch` y `validation_steps` a partir de `ds_info.splits['train'].num_examples` y el 80/20.

7. Entrena el modelo:
   - `epochs=5`
   - Usa `train_ds` y `valid_ds`.

Este paso sirve como **baseline**: modelo muy simple que probablemente no logre muy buena accuracy, pero deja en su lugar todo el “plumbing” (datos → modelo → entrenamiento).

---

## 10. Definición de datasets de Training/Validation desde GCS (TFRecords)

Más adelante, la sección “Training y Validation datasets” vuelve al enfoque original de GCS:

1. Define ruta base de TFRecords de 331x331:
   - `gcs_path_base = "gs://flowers-public/tfrecords-jpeg-331x331/flowers"`

2. Crea lista de archivos de entrenamiento:
   - `training_filenames = [f"{gcs_path_base}{i:02d}-16.tfrec" for i in range(16)]`
   - Construye nombres tipo `flowers00-16.tfrec`, `flowers01-16.tfrec`, ..., `flowers15-16.tfrec`.

3. Usa la misma lista para validación (`validation_filenames = training_filenames`, en este ejemplo).

4. Define `get_batched_dataset(filenames, train=False)`:
   - Carga el dataset con `load_dataset(filenames)`.
   - `cache()` en RAM.
   - Si `train=True`: `repeat()` para proveer datos indefinidamente (posible `shuffle()` comentado).
   - `batch(BATCH_SIZE)` y `prefetch(AUTOTUNE)`.

5. Instancia:
   - `training_dataset = get_batched_dataset(..., train=True)`
   - `validation_dataset = get_batched_dataset(..., train=False)`

6. Cuenta cuántas imágenes hay:
   - Itera sobre `load_dataset(training_filenames)` y `load_dataset(validation_filenames)` para calcular `num_train` y `num_valid`.

7. Calcula:
   - `steps_per_epoch = num_train // BATCH_SIZE`
   - `validation_steps = num_valid // VALIDATION_BATCH_SIZE`
   - Imprime los conteos y los batches por epoch.

*(En la práctica, si no tienes acceso al bucket GCS, esta parte puede fallar; el bloque con `tfds` es la alternativa local.)*

---

## 11. Definición del modelo preentrenado (Transfer Learning)

### a) Carga del modelo base preentrenado

- Selecciona MobileNetV2:
  ```python
  pretrained_model = tf.keras.applications.MobileNetV2(
      input_shape=[*IMAGE_SIZE, 3],
      include_top=False
  )
  pretrained_model.trainable = False
  ```
- Es un modelo pre-entrenado (típicamente en ImageNet), **sin la última capa softmax**, y con los pesos congelados.

### b) Arquitectura final

Dentro de `strategy.scope()`:

- Crea un modelo `Sequential` con:
  1. `pretrained_model`
  2. `GlobalAveragePooling2D()` → reduce mapas de activación a un vector 1D.
  3. `Dense(128, activation='relu')` → capa densa intermedia.
  4. `Dense(len(CLASSES), activation='softmax')` → capa de salida con 5 clases.

Este es el modelo de **transfer learning**: reutiliza MobileNetV2 como extractor de características y solo entrena la parte superior.

### c) Compilación

- `optimizer='adam'`
- `loss='sparse_categorical_crossentropy'`
- `metrics=['accuracy']`

### d) Sumario

- `model.summary()` imprime la arquitectura, número de parámetros, etc.

---

## 12. Entrenamiento del modelo de Transfer Learning

- Entrena el modelo con:
  ```python
  history = model.fit(
      training_dataset,
      steps_per_epoch=steps_per_epoch,
      epochs=EPOCHS,
      validation_data=validation_dataset
  )
  ```
- Usa los datasets basados en TFRecords (los de GCS), y el número de pasos calculado antes.
- Entrena durante `EPOCHS = 12`.

---

## 13. Evaluación y curvas de entrenamiento

- Evalúa el modelo:
  ```python
  print(model.evaluate(validation_dataset))
  ```
- Imprime las claves del historial de entrenamiento:
  - `history.history.keys()` → `accuracy`, `val_accuracy`, `loss`, `val_loss`, etc.
- Dibuja curvas:
  - `display_training_curves(history.history['accuracy'], history.history['val_accuracy'], 'accuracy', 211)`
  - `display_training_curves(history.history['loss'], history.history['val_loss'], 'loss', 212)`

Esto permite ver cómo evolucionan accuracy y loss en train/valid durante las épocas.

---

## 14. Predicciones y visualización de resultados

- Toma un lote aleatorio de 9 imágenes desde los TFRecords de validación:
  - Usa `load_dataset(validation_filenames)` y `skip(np.random.randint(300))` para saltar un número aleatorio de ejemplos.
  - Convierte a NumPy con `dataset_to_numpy_util(..., 9)`.

- Hace predicciones:
  ```python
  predictions = model.predict(flowers, steps=1)
  print(np.array(CLASSES)[np.argmax(predictions, axis=-1)].tolist())
  ```

- Muestra 9 imágenes con sus predicciones y marca en rojo las incorrectas:
  ```python
  display_9_images_with_predictions(flowers, predictions, labels)
  ```

---
