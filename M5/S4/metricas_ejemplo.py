import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, precision_score, accuracy_score, recall_score, roc_curve, roc_auc_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression

# 1. carga de datos
df_reg = pd.read_csv('datos_regresion.csv')
df_classi = pd.read_csv('datos_clasificacion.csv')

# 2. evaluar modelo de regresión
df_reg['Categoria'] = LabelEncoder().fit_transform(df_reg['Categoria'])

# datos de entrenamiento y test
X_reg = df_reg.drop('Valor_Ventas', axis=1)
y_reg = df_reg['Valor_Ventas']

# separar datos en entrenamiento y prueba
Xreg_train, Xreg_test, yreg_train, yreg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Entrenamiento del modelo
reg_model = LinearRegression()
reg_model.fit(Xreg_train, yreg_train)
y_pred_reg = reg_model.predict(Xreg_test)

# métricas de error para evaluar el modelo
mae_reg = mean_absolute_error(yreg_test, y_pred_reg)
mse_reg = mean_squared_error(yreg_test, y_pred_reg)
r2_score_reg = r2_score(yreg_test, y_pred_reg)
rmse_reg = np.sqrt(mse_reg)

print(f'mae_reg : {mae_reg:.2f}')
print(f'mse_reg : {mse_reg:.2f}')
print(f'rmse_reg : {rmse_reg:.2f}')
print(f'r2_score_reg : {r2_score_reg:.2f}')

# interpretación
print(f'El mae indica que el modelo tiene una prediccion de {mae_reg:.2f} unidades de venta')
print(f'El rmse penaliza los errores grandes y muestra {rmse_reg:.2f} unidades de venta')
print(f'El modelo tiene un ajuste de {r2_score_reg:.2f} logrando una varianza de ventas cercana a 1')

# 3. evaluar modelo de clasificación

# datos de entrenamiento y test
X_logreg = df_classi.drop('Comprara', axis=1)
y_log_reg = df_classi['Comprara']


# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_logreg, y_log_reg, test_size=0.2, random_state=42)

# Escalado de variables
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrenamiento del modelo
logreg = LogisticRegression()
logreg.fit(X_train_scaled, y_train)
y_pred = logreg.predict(X_test_scaled)

# Predicción y evaluación
y_proba_log = logreg.predict_proba(X_test_scaled)[:, 1]
print('Exactitud:', accuracy_score(y_test, y_pred))
print('Matriz de confusión: \n', confusion_matrix(y_test, y_pred))
print('Precisión:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('Roc AUC: ', roc_auc_score(y_test, y_proba_log))

'''
---

### 1. `y_proba_log = logreg.predict_proba(X_test_scaled)[:, 1]`
- **¿Qué es?**  
  Calcula la probabilidad de que cada instancia de prueba pertenezca a la clase positiva (por ejemplo, "sí compra").
- **¿Para qué sirve?**  
  Se usa para métricas como ROC AUC y para tomar decisiones basadas en probabilidades.

---

### 2. `accuracy_score(y_test, y_pred)`
- **Exactitud (Accuracy):**  
  Es el porcentaje de predicciones correctas sobre el total de casos.
- **¿Para qué sirve?**  
  Mide qué tan bien el modelo clasifica en general, pero puede ser engañosa si las clases están desbalanceadas.

---

### 3. `confusion_matrix(y_test, y_pred)`
- **Matriz de confusión:**  
  Es una tabla que muestra cuántos casos fueron clasificados correctamente o incorrectamente en cada clase.
- **¿Para qué sirve?**  
  Permite ver los errores específicos del modelo: falsos positivos, falsos negativos, verdaderos positivos y verdaderos negativos.

---

### 4. `precision_score(y_test, y_pred)`
- **Precisión (Precision):**  
  Es la proporción de verdaderos positivos sobre el total de predicciones positivas.
- **¿Para qué sirve?**  
  Indica cuántas de las predicciones positivas realmente lo son. Es útil cuando el costo de un falso positivo es alto.

---

### 5. `recall_score(y_test, y_pred)`
- **Recall (Sensibilidad):**  
  Es la proporción de verdaderos positivos sobre el total de casos positivos reales.
- **¿Para qué sirve?**  
  Mide la capacidad del modelo para encontrar todos los casos positivos. Es útil cuando el costo de un falso negativo es alto.

---

### 6. `roc_auc_score(y_test, y_proba_log)`
- **ROC AUC:**  
  Es el área bajo la curva ROC, que mide la capacidad del modelo para distinguir entre clases.
- **¿Para qué sirve?**  
  Un valor cercano a 1 indica que el modelo separa bien las clases; 0.5 indica que no es mejor que el azar.

---
'''