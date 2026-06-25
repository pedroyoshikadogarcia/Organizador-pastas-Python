import os
import shutil

CAMINHO_PASTA = r"C:\Users\pedro\OneDrive\Área de Trabalho\Garagem_Testes"
arquivos = os.listdir(CAMINHO_PASTA)

print ("Arquivos encontrados:")
for arquivo in arquivos:
    print (arquivo)