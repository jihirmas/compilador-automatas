import pandas as pd

data_mundiales = []

#leer txt
with open('datos.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)
    

print(data_mundiales)