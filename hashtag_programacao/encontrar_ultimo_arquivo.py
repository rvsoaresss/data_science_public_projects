import os
caminho = r'C:\Users\soaresdo\HP Inc\RawData_Surveys_Onsite - Documents'
lista_arquivos = os.listdir(caminho)

lista_datas = []
for arquivo in lista_arquivos:
    # descobrir a data desse arquivo
    if ".xlsx" in arquivo:
        data = os.path.getmtime(f"{caminho}\{arquivo}")
        lista_datas.append((data, arquivo))
        
lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]

ultimo_arquivo_nome = (f"{caminho}\{ultimo_arquivo[1]}")
print(ultimo_arquivo_nome)
ultimo_arquivo_nome_renomeado = r'C:\Users\soaresdo\HP Inc\RawData_Surveys_Onsite - Documents\TCE AMS Raw Data Commercial - 2021-11.xlsx'
print("arquivo renomeado")
os.replace(ultimo_arquivo_nome,ultimo_arquivo_nome_renomeado)