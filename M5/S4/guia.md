**Resumen explicativo de cada punto:**

---

**Regresión logística:**
Es un algoritmo de clasificación supervisada que estima la probabilidad de pertenencia a una clase usando la función sigmoídea, que transforma valores reales en probabilidades entre 0 y 1.
*Ventajas:* simple, interpretable y eficiente.
*Desventajas:* solo modela relaciones lineales y es sensible a outliers.
*Implementación en Python:* se usa `LogisticRegression` de scikit-learn.

---

**K-Nearest Neighbors (K-NN):**
Clasifica un dato según la mayoría de sus k vecinos más cercanos en el espacio de características.
*Escalamiento de datos:* es fundamental porque K-NN depende de distancias; se recomienda normalizar o estandarizar.
*Distancia euclideana:* es la métrica más común para medir cercanía entre puntos.
*Selección de k:* se prueba con varios valores y se elige el que da mayor exactitud.

---

**Árbol de decisión:**
Modelo que divide los datos en ramas según reglas basadas en las características, hasta llegar a una predicción.
*Hiperparámetros principales:* profundidad máxima (`max_depth`), mínimo de muestras por nodo (`min_samples_split`, `min_samples_leaf`).
*Medidas de impureza:* índice de Gini y entropía, que evalúan la pureza de los nodos.
*Ventajas:* interpretables y no requieren escalamiento.
*Desventajas:* pueden sobreajustar.
*Implementación en Python:* se usa `DecisionTreeClassifier`.

---

**Bosques aleatorios:**
Ensamble de muchos árboles de decisión entrenados sobre subconjuntos aleatorios de los datos (bagging), lo que mejora la precisión y reduce el sobreajuste.

---

**Support Vector Machine (SVM):**
Algoritmo que busca el hiperplano que mejor separa las clases maximizando el margen entre ellas.
*Funcionamiento:* utiliza vectores de soporte y puede aplicar funciones kernel para separar datos no lineales.
*Aplicación:* útil en clasificación binaria y multiclase, especialmente con datos complejos.
*Tipos de kernel:* lineal (para datos separables), polinómico, radial (RBF, para relaciones no lineales) y sigmoide.
