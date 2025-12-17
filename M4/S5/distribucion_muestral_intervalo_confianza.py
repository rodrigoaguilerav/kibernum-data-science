"""
Distribución muestral, LLN y CLT
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# 1. Conceptos básicos de distribución muestral
print("""
1. Conceptos básicos de distribución muestral
------------------------------------------------
La distribución muestral es la distribución de un estadístico (por ejemplo, la media) calculado a partir de muchas muestras aleatorias extraídas de una población. 
- La distribución de la población describe cómo se distribuyen los valores de todos los individuos de la población.
- La distribución de una muestra describe los valores de los individuos en una sola muestra.
- La distribución muestral describe cómo varía un estadístico (como la media) de muestra en muestra.
""")

# 2. Ley de los grandes números
print("""
2. Ley de los grandes números
-----------------------------
Se lanza una moneda equilibrada 10 veces y se obtiene cara en 7 de ellas.
¿Este resultado contradice la ley de los grandes números?
Respuesta:
No, este resultado no contradice la ley de los grandes números. La ley de los grandes números dice que, al aumentar el número de lanzamientos, la proporción de caras tenderá a 0.5. En pocas repeticiones (como 10), es normal observar desviaciones. Si repitiéramos muchas veces, la proporción se acercaría a 0.5.
""")

# 3. Teorema del límite central
print("""
3. Teorema del límite central
-----------------------------
El tiempo promedio de espera en una fila de banco sigue una distribución uniforme entre 5 y 15 minutos. Se toma una muestra aleatoria de 36 clientes.
- ¿Por qué es útil el teorema del límite central?
El teorema del límite central (TLC) es útil porque, aunque la población tiene una distribución uniforme (no normal), la distribución de las medias muestrales de tamaño 36 será aproximadamente normal. Esto permite usar métodos inferenciales basados en la normalidad.
""")

# Cálculo de la media y desviación estándar de la distribución muestral de la media
import numpy as np

# Parámetros de la distribución uniforme
minimo = 5
maximo = 15
n = 36

media_poblacional = (minimo + maximo) / 2
varianza_poblacional = ((maximo - minimo) ** 2) / 12
std_poblacional = np.sqrt(varianza_poblacional)

# Distribución muestral de la media
media_muestral = media_poblacional
std_muestral = std_poblacional / np.sqrt(n)

print(f"Media de la distribución muestral de la media: {media_muestral:.2f} minutos")
print(f"Desviación estándar de la distribución muestral de la media: {std_muestral:.2f} minutos\n")

# Gráfico: Simulación del TLC con distribución uniforme
medias_muestrales = [np.mean(np.random.uniform(minimo, maximo, n)) for _ in range(1000)]
plt.figure(figsize=(8, 5))
sns.histplot(medias_muestrales, bins=20, color='purple', edgecolor='black', stat='density', kde=True)
plt.title('Distribución muestral de la media (TLC, uniforme)')
plt.xlabel('Media muestral')
plt.ylabel('Densidad')
plt.grid(True)
plt.show()

# 4. Cálculo de probabilidades con la distribución muestral
print("""
4. Cálculo de probabilidades con la distribución muestral
--------------------------------------------------------
La duración de una llamada telefónica en una empresa sigue una distribución normal con media 8 minutos y desviación estándar 2 minutos. Se selecciona una muestra aleatoria de 25 llamadas.
Calcula la probabilidad de que el tiempo promedio de duración de la muestra sea menor a 7.5 minutos.
""")

from scipy.stats import norm

mu = 8
sigma = 2
n = 25
media_muestral = mu
std_muestral = sigma / np.sqrt(n)

# Probabilidad de que la media muestral sea menor a 7.5
z = (7.5 - media_muestral) / std_muestral
prob = norm.cdf(z)

print(f"Z = {z:.2f}")
print(f"Probabilidad de que la media muestral sea menor a 7.5 minutos: {prob:.4f}")

# intervalos de confianza
print("""
Intervalos de confianza
-----------------------
Para calcular un intervalo de confianza del 95% para la media muestral, utilizamos la fórmula:
IC = media_muestral ± Z * std_muestral
Donde Z es el valor crítico de la distribución normal estándar para un nivel de confianza del 95%.
""")
# Intervalo de confianza del 95%
z_95 = norm.ppf(0.975)  # Valor crítico para 95% de confianza
ic_inferior = media_muestral - z_95 * std_muestral
ic_superior = media_muestral + z_95 * std_muestral
print(f"Intervalo de confianza del 95%: ({ic_inferior:.2f}, {ic_superior:.2f}) minutos\n")

# Gráfico: Distribución normal de la media muestral y área de probabilidad
x = np.linspace(mu - 4*std_muestral, mu + 4*std_muestral, 200)
pdf = norm.pdf(x, loc=mu, scale=std_muestral)
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, color='blue', label='Distribución de la media muestral')
plt.fill_between(x, pdf, where=(x <= 7.5), color='blue', alpha=0.3, label='P(X̄ < 7.5)')
plt.axvline(7.5, color='red', linestyle='--', label='7.5 minutos')
plt.title('Probabilidad de media muestral < 7.5 minutos')
plt.xlabel('Media muestral (minutos)')
plt.ylabel('Densidad')
plt.legend()
plt.grid(True)
plt.show()