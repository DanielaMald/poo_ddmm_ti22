import pandas as pd
from openpyxl import Workbook
productos = pd.DataFrame({'SKU' : ['7501130935024','677702035457639' , '7702018913664'] , 
                          'Nombre' : ['helado holanda chocolate' , 'crema corporal lubridem', 'desodorante gel gillette'] ,
                          'Unidad' : ['Mililitros','Gramos', 'Gramos']})

libro = Workbook()
hoja = libro.active
hoja.title = 'Productos'
encabezados = ['SKU', 'Nombre', 'Unidad']
for i, encabezado in enumerate(encabezados, start=1):
    hoja.cell(row=1, column=i, value=encabezado)
for fila in productos.itertuples():
    datos_fila= [fila.SKU, fila.Nombre, fila.Unidad]
    hoja.append(datos_fila)
libro.save('demo.xlsx')
    
                          


