import time
import os
import pandas as pd

tempo_inicial=time.time()

arquivos=os.listdir()

for arquivo in arquivos:
    if "xlsx" in arquivo:
        tabela=pd.read_excel(arquivo)
        faturamento=tabela["Valor Final"].sum()
        print(f"Faturmanento da Loja {arquivo.replace('.xlsx','')} foi de {faturamento:,.2f}")

print(f"Demorou: {time.time()-tempo_inicial}")