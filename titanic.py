#Importo la libreria necesaria para la practica
import pandas as pd

#Generar un DataFrame con los datos del archivo.
titanic_df=pd.read_csv('titanic.csv') #Leo el archivo que tengo en mi maquina y lo hago un dataframe

#Mostrar por pantalla las dimensiones del DataFrame, 
#el número de datos que contiene, 
#los nombres de sus columnas y filas, 
#los  tipos de datos de las columnas, 
#las 10 primeras filas y las 10 últimas filas
print('\n////// CARACTERISTICAS DEL DATAFRAME //////')
print('Dimension del Dataframe:',titanic_df.shape)
print('Numero de Datos:',titanic_df.size)
print('Nombre de las Columnas:',titanic_df.columns.to_list())
print('Tipo de las Columnas:\n',titanic_df.dtypes)
print('Primeras 10 filas:\n',titanic_df.head(10))
print('Ultimas 10 filas:\n',titanic_df.tail(10))

#Mostrar por pantalla los datos del pasajero con identificador 148.
print('\n////// PASAJERO 148 //////')
print('Pasajero con id 148:\n',titanic_df[titanic_df['PassengerId']==148])

#Mostrar por pantalla las filas pares del DataFrame.
print('\n////// FILAS PARES //////')
print('Filas pares del data frame:\n',titanic_df[::2])

#Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print('\n////// NOMBRES ORDENADOS EN PRIMERA CLASE //////')
class1_df=titanic_df[titanic_df['Pclass']==1]
print('Nombres ordenados de los de primera clase:\n',class1_df['Name'].sort_values())

#Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print('\n////// PORCENTAJE DE SOBREVIVIENTES Y MUERTOS //////')
num_sobrevivientes=titanic_df[titanic_df['Survived']==1].shape[0]
num_muertos=titanic_df[titanic_df['Survived']==0].shape[0]
print('Porcentaje de sobrevivientes:',num_sobrevivientes/titanic_df.shape[0]*100,'%')
print('Porcentaje de muertes :',num_muertos/titanic_df.shape[0]*100,'%')

#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
print('\n////// PORCENTAJE DE SOBREVIVIENTES POR CLASE //////')
class2_df=titanic_df[titanic_df['Pclass']==2]
class3_df=titanic_df[titanic_df['Pclass']==3]

num_class1=class1_df.shape[0]
num_sobrevivientes_class1=class1_df[class1_df['Survived']==1].shape[0]
print('Porcentaje de sobrevivientes en clase 1:',((num_sobrevivientes_class1/num_class1)*100),'%')

num_class2=class2_df.shape[0]
num_sobrevivientes_class2=class2_df[class2_df['Survived']==1].shape[0]
print('Porcentaje de sobrevivientes en clase 2:',((num_sobrevivientes_class2/num_class2)*100),'%')

num_class3=class3_df.shape[0]
num_sobrevivientes_class3=class3_df[class3_df['Survived']==1].shape[0]
print('Porcentaje de sobrevivientes en clase 3:',((num_sobrevivientes_class3/num_class3)*100),'%')

#Eliminar del DataFrame los pasajeros con edad desconocida.
print('\n////// ELIMINAR EDADES DESCONOCIDAS //////')
titanic_clean=titanic_df.dropna(subset=['Age'])
print('Dimensiones del dataframe limpiado:',titanic_clean.shape)

#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print('\n////// EDAD MEDIA DE MUJERES POR CLASE //////')
mujeres_df=titanic_clean[titanic_clean['Sex']=='female']

print('Edad media de mujeres en clase 1:',mujeres_df[mujeres_df['Pclass']==1]['Age'].mean().round())
print('Edad media de mujeres en clase 2:',mujeres_df[mujeres_df['Pclass']==2]['Age'].mean().round())
print('Edad media de mujeres en clase 3:',mujeres_df[mujeres_df['Pclass']==3]['Age'].mean().round())

#Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
print('\n////// ANADIR COLUMNA BOOLEANA DE MENOR DE EDAD //////')
titanic_clean['Adult']=titanic_clean['Age']>=18
print('Dataframe con la nueva columna "Adult":\n',titanic_clean)

#Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print('\n////// PORCENTAJE DE MENORES Y MAYORES DE EDAD SOBREVIVIENTES POR CLASE //////')
adultos_df=titanic_clean[titanic_clean['Adult']==True]
menores_df=titanic_clean[titanic_clean['Adult']==False]

adult_class1=adultos_df[adultos_df['Pclass']==1].shape[0]
adult_survived_class1=adultos_df[adultos_df['Survived']==1][adultos_df['Pclass']==1].shape[0]
minor_class1=menores_df[menores_df['Pclass']==1].shape[0]
minor_survived_class1=menores_df[menores_df['Survived']==1][menores_df['Pclass']==1].shape[0]
print('Porcentaje de sobrevivientes adultos en clase 1:',(adult_survived_class1/adult_class1)*100,'%')
print('Porcentaje de sobrevivientes menores en clase 1:',(minor_survived_class1/minor_class1)*100,'%')

adult_class2=adultos_df[adultos_df['Pclass']==2].shape[0]
adult_survived_class2=adultos_df[adultos_df['Survived']==1][adultos_df['Pclass']==2].shape[0]
minor_class2=menores_df[menores_df['Pclass']==2].shape[0]
minor_survived_class2=menores_df[menores_df['Survived']==1][menores_df['Pclass']==2].shape[0]
print('Porcentaje de sobrevivientes adultos en clase 2:', (adult_survived_class2/adult_class2)*100, '%')
print('Porcentaje de sobrevivientes menores en clase 2:', (minor_survived_class2/minor_class2)*100, '%')

adult_class3=adultos_df[adultos_df['Pclass']==3].shape[0]
adult_survived_class3=adultos_df[adultos_df['Survived']==1][adultos_df['Pclass']==3].shape[0]
minor_class3=menores_df[menores_df['Pclass']==3].shape[0]
minor_survived_class3=menores_df[menores_df['Survived']==1][menores_df['Pclass']==3].shape[0]
print('Porcentaje de sobrevivientes adultos en clase 3:', (adult_survived_class3/adult_class3)*100, '%')
print('Porcentaje de sobrevivientes menores en clase 3:', (minor_survived_class3/minor_class3)*100, '%')