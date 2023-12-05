import pandas as pd # Importacion estandar de la libreria Pandas
import numpy as np # Importacion estandar de la libreria NumPy
# Crear diferentes tipos de datos
labels = ['a','b','c'] # lista de eetiquetas
my_list = [10,20,30] # lista con valores
arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPyd = {'a':10,'b':20,'c':30} # Creacion de un diccionario

# Convertir una lista en series usando el metodo pd.Series
# observe que se crean los nombres con las posiciones de cada elemento
pd.Series(data=my_list)
# Convertir una lista en series usando el metodo pd.Series
# se puede ingresar el nombre de las posiciones
pd.Series(data=my_list,index=labels)
# No es necesario ingresar la palabra de 'data ='' en el argumento
pd.Series(my_list,labels)

# Convertir un arreglo en series usando el metodo pd.Series
pd.Series(arr)

# Convertir un arreglo en series indicando tambien los valores del index
pd.Series(arr,labels)

#Desde Listas
#Convertir una lista en series usando el metodo pd.Series
#se crean los nombres con las posiciones de cada elemento
a=pd.Series(data=my_list)
print(a)
print(type(a));
print(pd.Series(my_list,index=labels))
print(type(a));
#Creando serie 1
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
#Crear serie 2
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   
a=ser2['Germany']
print(a)
a=ser1+ser2
print(a)
