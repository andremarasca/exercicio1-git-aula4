#!/home/marasca/anaconda3/bin/python3

import pandas as pd

df_sample = pd.read_csv("data/2006-sample.csv", encoding="latin-1", dtype=str)

# Selecionar nomes unicos de todas as companhias

unique_carrier = df_sample["UniqueCarrier"].unique()

# Criar um dicionario com os valores de contagem zerados

dict_total_time = {}

for uc in unique_carrier:
    dict_total_time[uc] = 0

# iterar as linhas e contar

for idx, row in df_sample.iterrows():
    uc = row["UniqueCarrier"]
    atraso = float(row["DepDelay"])
    if atraso > 0:
        dict_total_time[uc] += atraso

print(dict_total_time)
max_key = max(dict_total_time, key=dict_total_time.get)
print(f"Maximo: {max_key} com atraso de {dict_total_time[max_key]}")
