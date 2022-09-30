import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter

archivo = pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data = pd.DataFrame(archivo, columns=['CustomerKey', 'FirstName', 'TotalChildren'])
r1 = data.dropna(axis=0)
destino = ExcelWriter('resultados1.xlsx')
r1.to_excel(destino, index=False)
destino.save()
print('Ok')
