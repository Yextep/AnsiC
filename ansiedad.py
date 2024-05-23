import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Obtener la ubicación del script en ejecución
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar los datos desde un archivo Excel
file_path = os.path.join(current_dir, 'ansiedad_datos.xlsx')
df = pd.read_excel(file_path)

# Calcular el total de ansiedad sumando las columnas relevantes
df['total_ansiedad'] = df[['preocupacion', 'respuestas_fisiologicas', 'situaciones', 'respuestas_evitacion']].sum(axis=1)

# Asumiendo que ya tienes una columna llamada 'total_prueba_matematicas' en tu archivo Excel
# Si no la tienes, puedes agregar los datos manualmente o calculándolos de alguna manera similar a 'total_ansiedad'
# Aquí se asume que 'total_prueba_matematicas' ya está en el DataFrame.

# Graficar los datos individuales
plt.figure(figsize=(10, 6))

# Preocupacion
plt.subplot(2, 2, 1)
sns.histplot(df['preocupacion'], bins=10, kde=True)
plt.title('Preocupación')

# Respuestas Fisiológicas
plt.subplot(2, 2, 2)
sns.histplot(df['respuestas_fisiologicas'], bins=10, kde=True)
plt.title('Respuestas Fisiológicas')

# Situaciones
plt.subplot(2, 2, 3)
sns.histplot(df['situaciones'], bins=10, kde=True)
plt.title('Situaciones')

# Respuestas de Evitación
plt.subplot(2, 2, 4)
sns.histplot(df['respuestas_evitacion'], bins=10, kde=True)
plt.title('Respuestas de Evitación')

plt.tight_layout()

# Guardar la figura como una imagen en la ubicación actual
histogramas_output_path = os.path.join(current_dir, 'ansiedad_datos_histogramas.png')
plt.savefig(histogramas_output_path)

# Calcular y graficar la correlación
corr = df[['preocupacion', 'respuestas_fisiologicas', 'situaciones', 'respuestas_evitacion']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlación')

# Guardar la figura como una imagen en la ubicación actual
correlacion_output_path = os.path.join(current_dir, 'ansiedad_datos_correlacion.png')
plt.savefig(correlacion_output_path)

# Graficar la relación entre el total de ansiedad y el total de la prueba de matemáticas
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='total_ansiedad', y='total_prueba_matematicas')
plt.title('Relación entre el Total de Ansiedad y el Total de la Prueba de Matemáticas')
plt.xlabel('Total Ansiedad')
plt.ylabel('Total Prueba de Matemáticas')

# Guardar la figura como una imagen en la ubicación actual
relacion_output_path = os.path.join(current_dir, 'ansiedad_vs_matematicas.png')
plt.savefig(relacion_output_path)

# Guardar el DataFrame actualizado con las nuevas columnas en un nuevo archivo Excel en la ubicación actual
excel_output_path = os.path.join(current_dir, 'ansiedad_datos_actualizados.xlsx')
df.to_excel(excel_output_path, index=False)
