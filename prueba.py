
import pandas as pd
lista = ['matematicas','filosofia','historia','tecnologia']
nombres = ['alex', 'lucia','sara','roger']
notas_albert = [[6,9,3,7],[4,5,9,7],[8,3,8,5],[7,9,6,4]]
dataframe_tabla = pd.DataFrame(notas_albert,index = lista, columns = nombres)
dataframe_tabla


