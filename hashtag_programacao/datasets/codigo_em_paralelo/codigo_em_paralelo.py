from joblib import Parallel, delayed
import time
import pandas as pd
import os

tempo_inicial=time.time()

arquivos=os.listdir()

def calcular_faturamento(arquivo):
    if "xlsx" in arquivo:
        tabela=pd.read_excel(arquivo)
        faturamento=tabela["Valor Final"].sum()
        return f"Faturmanento da Loja {arquivo.replace('.xlsx','')} foi de {faturamento:,.2f}"

resultado = Parallel(n_jobs=2)(delayed(calcular_faturamento)(arquivo) for arquivo in arquivos)
print(resultado)
print(f"Demorou: {time.time()-tempo_inicial}")