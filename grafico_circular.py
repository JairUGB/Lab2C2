'''Este gráfico circular muestra la distribución de las ventas de videojuegos en todo el mundo por género. 
Es posible ver cuáles géneros han dominado el mercado a lo largo del tiempo y proporciona una imagen clara de 
las preferencias de los consumidores.'''

'''Enlace de dataset:
                        https://www.kaggle.com/datasets/thedevastator/global-video-game-sales'''

import pandas as pd
import matplotlib.pyplot as plt

video_game_data = pd.read_csv('vgsales.csv')

game_sales = video_game_data.groupby('Name')['Global_Sales'].sum().reset_index()

top_10_games = game_sales.sort_values(by='Global_Sales', ascending=False).head(10)

# Gráfico Circular
plt.figure(figsize=(8, 8))
plt.pie(top_10_games['Global_Sales'], labels=top_10_games['Name'], autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Ventas Globales por Videojuego (Top 10)')
plt.show()
