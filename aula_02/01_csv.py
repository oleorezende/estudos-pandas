# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df
# %%

df.to_csv("cliente.csv", index=False)



# %%

df.to_parquet("cliente.parquet", index=False)
# %%


df.to_excel("cliente.xlsx", index=False)
# %%
