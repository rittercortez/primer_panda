#############  Modulo PANDA  ###########
__________________________________________________________________________

############# SERIES ###########

ex:
    import pandas as pd
    asignatura = ['matematicas','ciencias','tecnologia']
    notas_lucia = [5,9,7]
    
    #Utilizamos la función 'Series' para crear una tabla de valores 'notas_lucia y de indice 'asignaturas'
    
    finales_lucia = pd.Series(notas_lucia,index=asignatura)

    #'.name'introduce el nombre a toda la tabla
    
    finales_lucia.name ='1r Trimestre'

    #'.index.name'  sirve para introducir el nombre a nuestro indice
    
    finales_lucia.index.name = 'Asignaturas'
    finales_lucia
    
    # utilizamos la función '.to_dict' para convertir nuestra 'Series'en diccionario
    
    diccionario_lucia = finales_lucia.to_dict() 
    diccionario_lucia
    
    #Podemos convertir un diccionario en una 'Series'
    
    serie_lucia = pd.Series(diccionario_lucia)
    serie_lucia



__________________________________________________________________________

############# DataFrames ###########

ex1: 
    import pandas as pd
    import webbrowser
    # Utilizamos el modulo 'webbrowser' para abrir el enlace web
    website = 'https://en.as.com/resultados/futbol/primera/clasificacion/'
    webbrowser.open(website)
    # La función '.read_clipboard()'recoger los datas actuales de 'crtl + C'
    dataframe_liga = pd.read_clipboard()
    dataframe_liga
    # Nos devuelve los nombre de la listas de las columnas
    dataframe_liga.columns

ex2:
    import pandas as pd
    lista = ['matematicas','filosofia','historia','tecnologia']
    notas_albert = [6,9,3,7]
    diccionario_albert = {'Asignaturas':lista , 'notas': notas_albert}
    diccionario_albert
    # Con la función 'DataFrame'creamos una tabla a partir de nuestro diccionario
    dataframe_notas = pd.DataFrame(diccionario_albert)
    dataframe_notas

__________________________________________________________________________

############# INDICES ###########

ex:     
    
    import pandas as pd
    lista = ['matematicas','filosofia','historia','tecnologia']
    nombres = ['alex', 'lucia','sara','roger']
    notas_albert = [[6,9,3,7],[4,5,9,7],[8,3,8,5],[7,9,6,4]]
    dataframe_tabla = pd.DataFrame(notas_albert,index = lista, columns = nombres)
    dataframe_tabla

__________________________________________________________________________

############# ELIMINAR ELEMENTOS EN SERIES Y DATAFRAME ###########

ex:
    import pandas as pd
    import numpy  as np

    series = pd.Series(np.arange(6),index= ['z','x','c','v','b','n'])
    series
    # la funcion '.drop'permite borrar la fila 'v' en este caso
    series.drop('v')

    contenido_lista = np.arange(12).reshape(3,4)
    fila = ['a','b','q']
    columna = ['x1','x2','x3','x4']
    dataframe = pd.DataFrame(contenido_lista, index=fila, columns=columna)
    dataframe

    borrar_fila = dataframe.drop('b')
    borrar_fila

    #la funcion 'axis'nos permite indicarle exactamente en que fila esta la columna que queremos borrar
    borrar_columna = dataframe.drop('x3', axis=1)
    borrar_columna


__________________________________________________________________________

############# SELECCIONAR DATOS EN DataFrame ###########

    # 'dataframe'es una funcion que creamos para hacer toda la tabla , '.loc' es una funcion que sirve LOCALIZAR datos atravez del indice que seleccionamos, '['i3'] cogera todo el indice de la fila 3
    
    - dataframe.loc['i3']       

    # Hace la misma función que lo explicado con anterioridad a diferencia que aqui vamos en busca de un valor que está en el indice ['i3'] y la columna ['c2']
    - dataframe.loc['i3']['c2'] 

    # Lo que hara es coger todos los valores de la tabla 'dataframe' y devolvernos los valores MAYORES  que 15
    - dataframe > 15 

ex : 
    import pandas as pd
    import numpy as np
    
    # Creamos 2 tablas DataFrame una con 16 valores y otra con 12 
    valores1 = np.arange(16).reshape(4,4)
    lista_indice1 = ['a','b','c','d']
    lista_columna = ['1','2','3','4']
    dataframe1 = pd.DataFrame(valores1, index=lista_indice1, columns = lista_columna)

    # 'list('abc') nos permite separar los elementos de una lista rapidamente
    lista_indice2 = list('abc')
    lista_columna2 = list('1234')
    valores = np.arange(12).reshape(3,4)
    dataframe2 = pd.DataFrame(valores, index= lista_indice2 , columns= lista_columna2)

    # Sumamos las dos tablas y los valores que no se puedan sumar nos dara de resultado 'NaN'
    dataframe = dataframe1 + dataframe2
    dataframe

    # Conn esta funcion conseguimos visualizar los valores que no se sumaron
    dataframe2.add(dataframe1, fill_value=0)


__________________________________________________________________________

############# ORDENACIÓN Y CLASIFICACIÓN ###########

ex: 
    import pandas as pd
    import numpy as np

    valores = np.random.randn(11)
    lista_indice = list('bimauqjklvc')
    serie = pd.Series(valores,index=lista_indice)

    # Ordena por la lista de INDICE
    serie.sort_index()

    # Ordena por la lista de VALORES
    serie.sort_values()


__________________________________________________________________________

############# ESTADISTICAS ###########

ex:
    import pandas as pd
    import numpy as np

    valores = np.array([[1,2,3],[4,5,6]])
    dataframe = pd.DataFrame(valores, index = list('ab'), columns= list('123'))
    # Sirve para ver el valor mas bajo de cada COLUMNA
    dataframe.min()

    # Sirve para ver el valor mas bajo de cada FILA
    dataframe.min(axis= 1)

    # Sirve para ver el valor mas alto de cada COLUMNA
    dataframe.max()

    # Sirve para ver el valor mas alto de cada FILA
    dataframe.max(axis= 1)

    # Sirve para sumar las COLUMNAS
    dataframe.sum()

    # Sirve para sumar las FILAS
    dataframe.sum(axis =1)

    # Sirve para  ver todas las funciones y  valores
    dataframe.describe()

__________________________________________________________________________

############# VALORES NULOS ###########

ex:
    import pandas as pd
    import numpy as np

    valores = [[np.nan,3,5],[6,np.nan,2],[9,7,8]]
    valores
    dataframe = pd.DataFrame(valores, index= [1,2,3], columns= list('abc'))
    # La función '.isnull()'sirve para identificar los valores nulos en la tabla
    dataframe.isnull()
    # BORRA todos las columnas que contienen valores NULOS
    dataframe.dropna(axis=1)
    # BORRA todas las filas que contiene valores NULOS
    dataframe.dropna()


__________________________________________________________________________

############# JERARQUIAS ###########
ex: 

    import pandas as pd
    import numpy as np
    # Creación de SERIES en >>> DATA FRAME
    listas_valores = np.random.rand(6)
    lista_indice = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
    serie = pd.Series(listas_valores, index=lista_indice)
    serie
    # Buscar en nuestra serie
    serie [1]['b']
    # Convertir nuestra serie en DATA FRAME utilizando la función '.unstack'
    convertido_AdataFrame = serie.unstack()

    # Convertir DATA FRAME en SERIE ####
    lista_value = np.arange(25).reshape(5,5)
    lista_index = [1,2,3,4,5]
    lista_column = ['A','B','C','D','E']
    dataframe = pd.DataFrame(lista_value, index = lista_index, columns= lista_column)
    # Utilizando la función '.stack'convertimos nuestro DATAFRAME  en SERIE
    dataframe.stack()