import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
import numpy as np

archivo = pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data = pd.DataFrame(archivo)
print('Resumir los valores perdidos totales')
res1 = data.isna().sum()
print(res1)
print('Obtener valores duplicados')
res2 = data.nunique()
print(res2)
print('Cantidad de veces que un cliente aparece en la BD')
res3 = data.groupby(by='CustomerKey').size().sort_values(ascending=False)
print(res3)
print('Eliminando valores dublicados')
res4 = data.drop_duplicates()
print(res4)
destino = ExcelWriter('resultados4.xlsx')
res4.to_excel(destino, index=False)
destino.save()
print('Ok')
