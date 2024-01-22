import os
import pandas as pd
import datapane as dp
import matplotlib.pyplot as plt
import numpy as np

base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "all_matches.csv")
df = pd.read_csv(csv_path)


# Partidos en los que ha participado España
partidosEspanaMundiales = df[((df['home_team'] == 'Spain') | (df['away_team'] == 'Spain')) & (df['tournament'] == 'World Cup')]

# Año de mundiales en los que participa España
partidosEspanaMundiales['year'] = pd.DatetimeIndex(partidosEspanaMundiales['date']).year

# Agrupar por año y sumar los goles
golesEspanaPorAno = partidosEspanaMundiales.groupby('year')['home_score', 'away_score'].sum()

# Crear una nueva columna con la suma total de goles por año
partidosEspanaMundiales['goles_espana'] = np.where(partidosEspanaMundiales['home_team'] == 'Spain', partidosEspanaMundiales['home_score'], partidosEspanaMundiales['away_score'])
golesEspanaPorAno = partidosEspanaMundiales.groupby('year')['goles_espana'].sum()

# Añadimos todos los años desde para que se vean incluso los que no ha jugado españa
todos_los_anos = pd.Series(np.arange(start=1930, stop=2023, step=4), name='year')

golesEspanaPorAno = todos_los_anos.to_frame().set_index('year').join(golesEspanaPorAno, how='left')
golesEspanaPorAno = golesEspanaPorAno.fillna(0)



# Crear el gráfico
fig, ax = plt.subplots()
ax.bar(golesEspanaPorAno.index, golesEspanaPorAno['goles_espana'])
plt.xticks(golesEspanaPorAno.index, rotation='vertical')
ax.set_yticks(np.arange(0, golesEspanaPorAno['goles_espana'].max()+1, 1))


# Crear diferentes formas de visualizar el informe
vista1 = dp.BigNumber(heading='GOLES TOTALES ESPAÑA EN LOS MUNDIALES', value=golesEspanaPorAno['goles_espana'].sum())
vista2 = dp.Group(dp.Table(partidosEspanaMundiales), label="Todos los partidos de España en los mundiales")
vista3 = dp.Group(dp.Plot(fig), label="Gráfico de goles de España en cada mundial")

# Crear un selector para las diferentes vistas
selector = dp.Select(vista1, vista2, vista3)


titulo = dp.HTML("<h1 style='color:blue;'>Informe de GOLES Seleccion Española</h1>")

report = dp.Report(titulo,selector)
report_path = os.path.join(base_path, "informe4.html")
report.save(report_path, open=True)





