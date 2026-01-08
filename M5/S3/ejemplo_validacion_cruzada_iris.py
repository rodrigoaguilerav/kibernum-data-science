# Importar librerías
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import (
KFold,
LeaveOneOut,
StratifiedKFold,
ShuffleSplit,
cross_val_score,
)
from sklearn.ensemble import RandomForestClassifier

# Cargar el dataset Iris
data = load_iris()
X = data.data # Características (features)
y = data.target # Etiquetas (labels)

'''
 Implementación de k-Fold Cross-Validation
'''
# Configurar k-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluar el modelo con k-Fold
model = RandomForestClassifier(random_state=42)
scores = cross_val_score(model, X, y, cv=kf)

# Mostrar los resultados
print("Puntuaciones de k-Fold Cross-Validation:", scores)
print("Puntuacion media:", np.mean(scores))

'''
Implementación de Leave-One-Out Cross-Validation (LOOCV)
'''
# Configurar Leave-One-Out Cross-Validation
loo = LeaveOneOut ()

# Evaluar el modelo con LOOCV
scores = cross_val_score(model, X, y, cv=loo)

# Mostrar los resultados
print("Puntuaciones de LOOCV:", scores)
print("Puntuacion media:", np.mean(scores) )

'''
Implementación de Random Subsampling (Monte Carlo Cross-Validation)
'''
# Configurar Random Subsampling
rs = ShuffleSplit(n_splits=10, test_size=0.2, random_state=42)

# Evaluar el modelo con Random Subsampling
scores = cross_val_score(model, X, y, cv=rs)

# Mostrar los resultados
print("Puntuaciones de Random Subsampling:", scores)
print("Puntuacion media:", np.mean(scores))

'''
Comparación de los métodos
'''
# Comparar resultados
print("Comparacion de métodos:")
print("k-fold:", np.mean(cross_val_score(model, X, y, cv=KFold(n_splits=5, shuffle=True, random_state=42))))
print("Loocv:", np.mean(cross_val_score(model, X, y, cv=loo)))
print("Random Subsampling:", np.mean(cross_val_score(model, X, y, cv=rs)))
# print("Random Subsampling:", np.mean(cross_val_score(model, X, y, cv=ShuffleSplit(n_splits=10, test_size=0.2, random_state=42))))