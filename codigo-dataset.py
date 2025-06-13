import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = "https://raw.githubusercontent.com/12natt23/codigo-parcial/main/processes.csv"

# Leer el dataset con encoding compatible
df = pd.read_csv(csv_file, encoding="latin1", on_bad_lines='skip')

# Convertir columnas numéricas
df['cpu_percent'] = pd.to_numeric(df['cpu_percent'], errors='coerce')
df['memory_percent'] = pd.to_numeric(df['memory_percent'], errors='coerce')

# Limpiar filas problemáticas
df_clean = df.dropna(subset=['cpu_percent', 'memory_percent'])

# Estadísticas básicas
print("\n Estadísticas básicas:")
print("Media:\n", df_clean[['cpu_percent', 'memory_percent']].mean())
print("\nMediana:\n", df_clean[['cpu_percent', 'memory_percent']].median())
print("\nModa:\n", df_clean[['cpu_percent', 'memory_percent']].mode().iloc[0])
print("\nDesviación estándar:\n", df_clean[['cpu_percent', 'memory_percent']].std())

# Matriz de correlación
corr_matrix = df_clean[['cpu_percent', 'memory_percent']].corr()
print("\n Matriz de correlación:")
print(corr_matrix)

# Gráfica de matriz de correlación
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de correlación entre CPU % y Memoria %")
plt.show()
