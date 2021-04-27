import pandas as pd

df_sample = pd.read_csv("data/2006-sample.csv", encoding="latin-1", dtype=str)

# Criar um dicionario (chave: Nome do aeropoto, conteúdo: lista vazia)

dict_origin_dest = {}

for key in df_sample["Origin"].unique():
    dict_origin_dest[key] = []

# Iterar o DataFrame populando o dicionário dict_origin_dest

for idx, row in df_sample.iterrows():
    dict_origin_dest[row["Origin"]].append(row["Dest"])

# Imprimir o dicionario dict_origin_dest

for key in dict_origin_dest:
    print("Origem", key, "==> Destino:",
          ", ".join(dict_origin_dest[key]), "\n")
