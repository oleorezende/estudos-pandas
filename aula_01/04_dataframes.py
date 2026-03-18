# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_idades

# %%

df = pd.DataFrame()
df["Idades"] = series_idades
df["Nomes"] = series_nomes
df
# %%
df["Nomes"]
# %
# %%
df.iloc[0]
# %%
