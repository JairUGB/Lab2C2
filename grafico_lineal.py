'''El código visualiza la evolución de la población mundial a lo largo de los años en un gráfico de líneas, 
proporcionando una representación clara del crecimiento poblacional.'''

'''Enlace de dataset: 
                        https://www.kaggle.com/datasets/yusufglcan/country-data'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('worldPopulation.csv')

print(data.head())

plt.figure(figsize=(12, 6))
plt.plot(data['Year'], data['Population'], marker='o', color='purple')
plt.title('Evolución de la Población Mundial')
plt.xlabel('Año')
plt.ylabel('Población (en miles de millones)')
plt.grid(True)

plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()
plt.show()