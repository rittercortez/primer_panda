import pandas as pd
# Buscamos el archivo excel y leemos su contenido
archivo = pd.read_excel('/Users/thehome/Desktop/poblacion.xlsx')
# Lo transformamos en DATA FRAME
datos = pd.DataFrame(archivo)
print(datos)
# Permite ver todas los encabezados de las columnas 
columna = datos.columns
print(columna)
# Muestra la primera fila del dataframe
fila1 = datos.head()
print(fila1)
# Mostrar la primera columna del dataframe
columna1 = datos["Continente"]
print(columna1)
# Mostrar todas las filas pero solo las columnas 'Continente' y 'Población'
cont_pobl = datos.loc[0:3,["Continente","Población"]]
print(cont_pobl)
# Mostrar las primeras 3 filas del dataframe
filas3 = datos.head(3)
print(filas3)
# Mostrar las 2 ultimas filas del dataframe
filas2 = datos.tail(2)
print(filas2)


