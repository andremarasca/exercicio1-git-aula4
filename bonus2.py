#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("2006-sample.csv", encoding="latin-1", dtype=str)


# In[5]:


aero = df["UniqueCarrier"].unique() #transformando os valores unicos do uniquecarrier (siglas de aeroportos) na variavel df


# In[6]:


contagem={}  # dicionario com os valores de contagem zerados


# In[8]:


for i in aero:
    contagem[i] = 0

# iterar as linhas e contar

for idx, row in df.iterrows():
    uc = row["UniqueCarrier"]
    atraso = float(row["DepDelay"])
    if atraso > 0:
        contagem[uc] += atraso

print(contagem)
max_key = max(contagem, key=contagem.get)
print(f"Maximo: {max_key} com atraso de {contagem[max_key]}")

