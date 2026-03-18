# %%
import pandas as pd
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers=headers)
resposta.raise_for_status()

dfs = pd.read_html(StringIO(resposta.text))
dfs

# %%
df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep=";", index=False)