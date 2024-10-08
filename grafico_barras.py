'''Este gráfico de barras muestra la popularidad promedio de cada canción por año.
Se puede ver cómo la popularidad ha cambiado con el tiempo, con picos en años específicos 
que podrían estar relacionados con tendencias musicales o cambios en las plataformas de música.'''

'''Enlace de dataset: 
                        https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset'''

import pandas as pd
import matplotlib.pyplot as plt

spotifyData = pd.read_csv('spotify_data.csv')

spotifySubset = spotifyData[['year', 'popularity']].groupby('year').mean().reset_index()

# Gráfico de barras
plt.figure(figsize=(15, 6))
plt.bar(spotifySubset['year'], spotifySubset['popularity'], color='blue')
plt.title('Popularidad Promedio de las Canciones por Año')
plt.xlabel('Año')
plt.ylabel('Popularidad Promedio')
plt.show()
