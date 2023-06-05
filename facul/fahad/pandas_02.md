<!-- no google colab pra dar certo -->

import pandas as pd

# Importando arquivo

url = "http://leg.ufpr.br/~walmes/data/euro_football_players.txt"
df = pd.read_table(url, sep = "\t", comment = "#" )

<!--  -->

df
-mostra toda a tabela do link

len(df)
-tamanho

df.dtypes
-media tabela

df.shape
-linhas e colunas

df.info
-info

df.column
-lista colunas

df["country"]
-mostra o country

type(df["country"])
pandas.core.series.Series

df[ ['country', 'team', 'age'] ]

df = df.rename(columns={"country": "pais" })
df.columns
