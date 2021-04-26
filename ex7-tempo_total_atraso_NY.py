#!/home/marasca/anaconda3/bin/python3

import pandas as pd

df_sample = pd.read_csv("data/2006-sample.csv", encoding="latin-1", dtype=str)

# Filtrar linhas referente a (JFK) Nova Iorque
df_sample_jfk = df_sample[:][df_sample["Origin"]=="JFK"]

# Coluna com os valores de DepDelay
serie_dep_delay = df_sample_jfk["DepDelay"]

# Conversão de string para float

serie_dep_delay = serie_dep_delay.apply(float)

# Filtrar valores positivos (atraso)
atrasos = serie_dep_delay[serie_dep_delay > 0]

# imprimir soma de atrasos
print(sum(atrasos))