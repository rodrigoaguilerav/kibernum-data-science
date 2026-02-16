## Guía rápida del flujo principal

### 1. Datos
1. **Carga local con `tensorflow_datasets` (`tf_flowers`)**
   - Descarga dataset.
   - Divide en **train (80%)** y **valid (20%)**.
   - `map(preprocess_local)` → redimensiona a 331×331 y normaliza `[0,1]`.
   - Crea `train_ds` y `valid_ds` con `cache()`, `shuffle()`, `batch()`, `prefetch()`.

2. **Carga desde TFRecords en GCS (formato original)**
   - `read_tfrecord()` decodifica imagen y etiqueta.
   - `load_dataset(filenames)` crea `tf.data.Dataset`.
   - `get_batched_dataset()` → `cache` → (si train: `repeat`) → `batch(BATCH_SIZE)` → `prefetch`.
   - Se obtienen `training_dataset` y `validation_dataset`.
   - Se calculan `steps_per_epoch` y `validation_steps`.

---

### 2. Modelo simple (baseline)
1. Define un `Sequential` muy sencillo:
   - `Flatten(input_shape=(331, 331, 3))`
   - `Dense(5, activation='softmax')`
2. Compila con:
   - `optimizer='adam'`
   - `loss='sparse_categorical_crossentropy'`
   - `metrics=['accuracy']`
3. Entrena:
   - `simple_model.fit(train_ds, validation_data=valid_ds, epochs=5, steps_per_epoch=..., validation_steps=...)`
4. Objetivo: tener un **baseline** y validar que todo el flujo de datos/ entrenamiento funciona.

---

### 3. Modelo con Transfer Learning
1. **Modelo base preentrenado**
   - `pretrained_model = MobileNetV2(input_shape=[*IMAGE_SIZE, 3], include_top=False)`
   - `pretrained_model.trainable = False` (congelado).

2. **Arquitectura final**
   - Dentro de `strategy.scope()`:
     - `Sequential([`
       - `pretrained_model,`
       - `GlobalAveragePooling2D(),`
       - `Dense(128, activation='relu'),`
       - `Dense(5, activation='softmax')`
       - `])`

3. **Compilación**
   - Igual que antes: `'adam'`, `sparse_categorical_crossentropy`, `accuracy`.

4. **Entrenamiento**
   - Usa los **TFRecords**:
   - `model.fit(training_dataset, steps_per_epoch=steps_per_epoch, epochs=EPOCHS, validation_data=validation_dataset)`

---

### 4. Evaluación y predicciones
1. **Evaluación global**
   - `model.evaluate(validation_dataset)` → loss y accuracy de validación.

2. **Curvas de entrenamiento**
   - `display_training_curves(history['accuracy'], history['val_accuracy'], ...)`
   - `display_training_curves(history['loss'], history['val_loss'], ...)`

3. **Predicciones visuales**
   - Toma 9 imágenes aleatorias de validación (TFRecords).
   - `model.predict(flowers)`
   - `display_9_images_with_predictions(flowers, predictions, labels)`  
   → ves qué flores acierta y cuáles falla, usando el modelo de **transfer learning**.