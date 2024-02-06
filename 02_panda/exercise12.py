# Notas:
# 
# Utilice la función pd.read_html() para acceder a las tablas. La tabla de superficie tiene el índice 3 y la tabla de población tiene el índice 4.
# 
# Elimine la última fila de totales en cada DataFrame y quédese sólo con las columnas que interesen.
# 
# Renombre las columnas según interese.
# 
# Reemplace los valores de población y superficie para que sean números y convierta las columnas a entero.
# 
# Realice la mezcla de población y superficie en un único DataFrame.
# 
# Calcule la densidad de población de cada comunidad autónoma.

import pandas as pd

URL = 'https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma'

tables = pd.read_html(URL)

df_surface = tables[3]
df_surface = df_surface.iloc[:-1, 1:3]
df_surface.columns = ('Comunidad', 'Superficie')

df_population = tables[4]
df_population = df_population.iloc[:-1, 1:3]
df_population.columns = ('Comunidad', 'Población')

df = pd.merge(df_surface, df_population)
df['Densidad'] = df['Población'] / df['Superficie']

print(df)