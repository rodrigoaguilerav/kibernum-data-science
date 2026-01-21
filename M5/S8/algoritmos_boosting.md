Algoritmos boosting
---

### 1. AdaBoost (Adaptive Boosting)
- **Idea:** Combina muchos clasificadores débiles (típicamente árboles muy pequeños, “stumps”) en un modelo fuerte.  
- **Cómo funciona:**  
  - Entrena un árbol simple.  
  - Aumenta el peso de las observaciones mal clasificadas.  
  - Repite el proceso y combina los modelos con un peso según su desempeño.  
- **Ventajas:** Sencillo, bueno para modelos base muy simples.  
- **Desventajas:** Sensible al ruido y a outliers.

---

### 2. Gradient Boosting
- **Idea:** Construye árboles secuencialmente para **corregir los errores** del modelo anterior usando gradiente descendente.  
- **Cómo funciona:**  
  - Empieza con una predicción inicial (por ejemplo, promedio).  
  - En cada iteración entrena un nuevo árbol sobre los **residuos** (error) del modelo actual.  
  - Suma todos los árboles (cada uno con un pequeño learning_rate).  
- **Ventajas:** Muy flexible y preciso.  
- **Desventajas:** Entrenamiento más lento, fácil de sobreajustar si no se regula.

---

### 3. XGBoost (Extreme Gradient Boosting)
- **Idea:** Implementación optimizada y regularizada de Gradient Boosting.  
- **Características clave:**  
  - Maneja regularización L1/L2 (reduce sobreajuste).  
  - Soporta manejo eficiente de valores faltantes.  
  - Usa paralelización y optimizaciones de bajo nivel (muy rápido).  
- **Ventajas:** Suele dar muy buen rendimiento en competencias y problemas tabulares.  
- **Desventajas:** Más complejo de configurar; muchos hiperparámetros.

---

### 4. LightGBM
- **Idea:** Otra implementación de Gradient Boosting diseñada para ser **muy rápida y escalable**.  
- **Características clave:**  
  - Usa árboles **leaf-wise** (crece por hojas, no por niveles), lo que mejora la pérdida más rápido.  
  - Maneja muy bien datasets grandes y muchas características categóricas.  
- **Ventajas:** Muy rápido, poco consumo de memoria, buen rendimiento.  
- **Desventajas:** Leaf-wise puede sobreajustar si no se controla (max_depth, min_data_in_leaf).  

---

Resumen rápido:
- **AdaBoost:** boosting clásico, simple, con pesos en las muestras.  
- **Gradient Boosting:** corrige errores mediante gradientes (árboles sobre residuos).  
- **XGBoost:** Gradient Boosting ultra optimizado y regularizado.  
- **LightGBM:** Gradient Boosting muy rápido y escalable, pensado para grandes volúmenes de datos.