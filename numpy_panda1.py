"""
Tenemos 3 clases 'clase1', 'clase2', 'clase3'
Vamos a generar un numero aleatorio de alumnos por clase
Para obtener un numero aleatorio utilizaremos
    (np.random.randint(minimo,maximo,numero))
Crear un serie de clase y alumnos
Utilizar el indice de la serie para saber el numero de alumnos de la clase2
"""
import pandas as pd
import numpy as np

clase1 = np.random.randint(0,100,1)
clase2 = np.random.randint(0,100,1)
clase3 = np.random.randint(0,100,1)
valor = [clase1,clase2,clase3]
indice = ['c1','c2','c3']
serie = pd.Series(valor,index=indice)
serie