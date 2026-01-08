## ¿Qué es una tarea de clasificación?

En aprendizaje automático, una **tarea de clasificación** consiste en predecir una categoría o clase para una instancia dada.

- Se habla de **clasificación binaria** cuando la variable objetivo (`Y`) tiene solamente dos categorías posibles (por ejemplo: `True/False`, `Sí/No`).
- Se habla de **clasificación multi-clase** cuando la variable objetivo (`Y`) tiene más de dos categorías posibles (por ejemplo: `Virginica`, `Versicolor`, `Setosa`).
- Se habla de **clasificación multi-etiqueta** cuando una instancia puede estar asociada a más de una clase o categoría al mismo tiempo (por ejemplo: `Enfermedad A`, `Enfermedad B`, `Enfermedad C`).

---



## **Actividad: Identificación del Tipo de Clasificación**


1. **A partir de la información demográfica y la cantidad de veces que un cliente ha sido expuesto a una publicidad, queremos saber si un cliente realizará una compra.→ Clasificación Binaria** (compra: sí/no)
2. **A partir de los textos de un correo electrónico, se desea entrenar un algoritmo que pueda determinar si un correo es spam.→ Clasificación Binaria** (spam/no spam)
3. **A partir de una fotografía del rostro de una persona, deseamos saber cuál es su nombre.→ Clasificación Multi-clase** (una clase por persona)
4. **A partir de información de temperatura, humedad, presión atmosférica y velocidad del viento, queremos predecir cómo estará el clima el día de mañana.→ Ninguna de las anteriores** (si el clima es una variable continua, es regresión; si son categorías como “soleado”, “lluvioso”, sería multi-clase, pero no está especificado)
5. **A partir de un texto, queremos clasificar los tópicos al cual pertenece.→ Clasificación Multi-etiqueta** (un texto puede tener varios tópicos)
7. **A partir de la información de cantidad de habitaciones, sector, metros cuadrados, cercanía al metro, dependencias, ubicación, año y material de construcción, queremos predecir el precio de un bien raíz**
   **→ Ninguna de las anteriores** (esto es un problema de regresión, no de clasificación)

**Resumen:**

1. Clasificación Binaria
2. Clasificación Binaria
3. Clasificación Multi-clase
4. Ninguna de las anteriores
5. Clasificación Multi-etiqueta
6. Ninguna de las anteriores
