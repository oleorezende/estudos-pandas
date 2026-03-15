# %%
idades = [
    20,
    30,
    40,
    50,
    60,
    80,
    11,
    22,
    33,
    44,
    55,
    66,
    17,
    18,
    19,
    31,
    35,
]

# média
media = sum(idades) / len(idades)

# variância
soma = 0

for idade in idades:
    soma += (idade - media) ** 2

variancia = soma / len(idades)

print("Média:", media)
print("Variância:", variancia)
# %%

import pandas as pd
# %%

series_idades = pd.Series(idades)
series_idades
# %%
# estatisticas da series

media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()

print (media_idades)
print (var_idades)
print (summary_idades)

# %%
