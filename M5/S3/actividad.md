- **clasificación binaria**: cuando la variable objetivo (`Y`) tiene solamente dos categorías posibles (por ejemplo: `True/False`, `Sí/No`).
- **clasificación multi-clase**: cuando la variable objetivo (`Y`) tiene más de dos categorías posibles (por ejemplo: `Virginica`, `Versicolor`, `Setosa`).
- **clasificación multi-etiqueta**: cuando una instancia puede estar asociada a más de una clase o categoría al mismo tiempo (por ejemplo: `Enfermedad A`, `Enfermedad B`, `Enfermedad C`).

---
# Actividad: Identificación de Problemas de Clasificación

---

**1. Problema a Resolver:**
Predecir si un paciente tiene diabetes.
**Features que utilizará:** Edad, IMC, presión arterial, nivel de glucosa, historial familiar, actividad física, diagnóstico de diabetes.
**Feature seleccionado:** 
**Variable Objetivo:** 
**Tipo de Clasificación:** 
**Algoritmo sklearn:** `LogisticRegression`

---

**2. Problema a Resolver:**
Clasificar correos electrónicos como spam o no spam.
**Features que utilizará:** Frecuencia de palabras clave, presencia de enlaces, longitud del correo, remitente, número de adjuntos, etiqueta de spam (Spam/No Spam). 
**Feature seleccionado:** 
**Variable Objetivo:** 
**Tipo de Clasificación:** 
**Algoritmo sklearn:** `MultinomialNB`

---

**3. Problema a Resolver:**
Predecir el tipo de animal en una imagen (perro, gato, ave).
**Features que utilizará:** Color, textura, forma, tamaño, tipo de animal
**Feature seleccionado:**
**Variable Objetivo:**
**Tipo de Clasificación:**
**Algoritmo sklearn:** `RandomForestClassifier`

---

**4. Problema a Resolver:**
Clasificar el sentimiento de una reseña de producto.
**Features que utilizará:** Texto de la reseña, puntuación, longitud, presencia de palabras positivas/negativas, sentimiento (Positivo/Negativo/Neutral).
**Feature seleccionado:** 
**Variable Objetivo:** 
**Tipo de Clasificación:**
**Algoritmo sklearn:** `MultinomialNB`

---

**5. Problema a Resolver:**
Predecir si un cliente abandonará el servicio (churn).
**Features que utilizará:** Tiempo como cliente, número de reclamos, uso mensual, tipo de contrato, edad, churn(tasa de cancelación).
**Feature seleccionado:** 
**Variable Objetivo:**
**Tipo de Clasificación:**
**Algoritmo sklearn:** `RandomForestClassifier`

---

**6. Problema a Resolver:**
Clasificar el género musical de una canción.
**Features que utilizará:** Tempo, duración, instrumentos, ritmo, tonalidad, género musical (Rock/Pop/Jazz/Clásica).
**Feature seleccionado:** 
**Variable Objetivo:** 
**Tipo de Clasificación:**
**Algoritmo sklearn:** `KNeighborsClassifier`

---

**7. Problema a Resolver:**
Predecir el nivel de riesgo crediticio de un solicitante.
**Features que utilizará:** Ingresos, historial crediticio, edad, empleo, deudas actuales, nivel de riesgo (Alto/Medio/Bajo).
**Feature seleccionado:** 
**Variable Objetivo:** 
**Tipo de Clasificación:** 
**Algoritmo sklearn:** `DecisionTreeClassifier`

---

**8. Problema a Resolver:**
Clasificar noticias en múltiples categorías.
**Features que utilizará:** Texto de la noticia, fuente, fecha, palabras clave, categoría de la noticia (Política/Deportes/Tecnología/Economía).
**Feature seleccionado:** 
**Variable Objetivo:**
**Tipo de Clasificación:** 
**Algoritmo sklearn:** `MultinomialNB`

---

**9. Problema a Resolver:**
Predecir si una transacción es fraudulenta.
**Features que utilizará:** Monto, hora, ubicación, tipo de comercio, historial del usuario, fraude (Sí/No).
**Feature seleccionado:** 
**Variable Objetivo:**
**Tipo de Clasificación:**
**Algoritmo sklearn:** `RandomForestClassifier`

---

**10. Problema a Resolver:**
Clasificar imágenes médicas según la presencia de múltiples enfermedades.
**Features que utilizará:** Características extraídas de la imagen, edad del paciente, historial médico, Enfermedades presentes (Enfermedad A, Enfermedad B, Enfermedad C, etc.).
**Feature seleccionado:** 
**Variable Objetivo:** 
**Tipo de Clasificación:** 
**Algoritmo sklearn:** `OneVsRestClassifier(RandomForestClassifier())`

---
