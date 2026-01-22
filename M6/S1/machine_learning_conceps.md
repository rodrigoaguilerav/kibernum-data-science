1. **Fundamentos del aprendizaje no supervisado**  
   - No hay variable objetivo: solo tenemos **X**, sin etiquetas **y**.  
   - El objetivo es **descubrir estructura** en los datos: grupos, patrones, anomalías, reducción de dimensión.  
   - Se usa cuando no tenemos etiquetas o son muy costosas de obtener.

2. **Clusterización (clustering)**  
   - Tarea de agrupar observaciones similares entre sí y diferentes de otros grupos.  
   - Cada grupo (cluster) intenta contener puntos “parecidos” según una medida de distancia o similitud.  
   - Ejemplos de uso: segmentación de clientes, agrupación de documentos, patrones en sensores.

3. **Clusterización jerárquica**  
   - Construye una **jerarquía de clusters** (árbol o dendrograma).  
   - Puede ser:
     - **Aglomerativa**: empieza con cada punto como cluster y va fusionando.  
     - **Divisiva**: empieza con un solo cluster y lo va dividiendo.  
   - No requiere fijar el número de clusters a priori; se decide “cortando” el dendrograma.

4. **K-Means**  
   - Algoritmo de clustering particional que divide los datos en **K clusters**.  
   - Minimiza la suma de distancias cuadradas de cada punto a su **centroide**.  
   - Requiere elegir K, es sensible a la escala de las variables y a outliers, y asume clusters “más o menos esféricos”.

5. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**  
   - Agrupa puntos en regiones de **alta densidad** y marca como “ruido” los puntos aislados.  
   - No necesita fijar K; sus parámetros clave son:
     - `eps`: radio de vecindad.  
     - `min_samples`: mínimo de puntos para formar un cluster denso.  
   - Detecta clusters de forma arbitraria y es robusto a outliers, pero requiere ajustar bien `eps` y `min_samples`.

6. **Análisis de Componentes Principales (PCA)**  
   - Técnica de **reducción de dimensión lineal**.  
   - Encuentra nuevas variables (componentes principales) que son combinaciones lineales de las originales y explican la máxima varianza.  
   - Se usa para:
     - Reducir número de features.  
     - Quitar correlación.  
     - Visualizar datos de alta dimensión en 2D/3D.

7. **t-SNE (t‑Distributed Stochastic Neighbor Embedding, a veces escrito “tSNE” o “TNSE”)**  
   - Técnica de **visualización** no lineal para datos de alta dimensión.  
   - Conserva bien las **relaciones locales** (vecinos cercanos) al proyectar a 2D/3D; muy usada para ver clusters.  
   - No es buena para reducir dimensión para modelar (ni para distancias globales), es costosa y tiene hiperparámetros sensibles (perplexity, learning rate).