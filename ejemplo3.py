import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
import numpy as np

archivo = pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data = pd.DataFrame(archivo, columns=['TotalChildren'])
promedio = data["TotalChildren"].mean()
res = data["TotalChildren"].replace(np.nan, promedio)
destino = ExcelWriter('resultados3.xlsx')
res.to_excel(destino, index=False)
destino.save()
print('Ok')
