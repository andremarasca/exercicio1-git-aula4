#!/home/marasca/anaconda3/bin/python3

import pandas as pd

df_sample = pd.read_csv("data/2006-sample.csv", encoding="latin-1", dtype=str)

# Filtrar instancias da companhia DL (Delta Air Lines)

df_dl_sample = df_sample[:][df_sample["UniqueCarrier"] == "DL"]

# Converter dados String em float

df_dl_sample["ArrDelay"] = df_dl_sample["ArrDelay"].apply(float)

# Selecionar valores positivos

df_dl_sample = df_dl_sample[:][df_dl_sample["ArrDelay"] > 0]

# Imprimir soma do atraso

print(sum(df_dl_sample["ArrDelay"]))