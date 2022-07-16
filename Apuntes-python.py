# Archivo procedente de la masterclass de Python de InformatiCódigo (https://youtube.com/c/InformatiCodigo)
'''
Índice:
    1. Básico de Python
        - ¿Qué es Python?
        - Comentarios
        - Comando print()
        - Variables y tipos de datos
            > int
            > float
            > complex
            > str
            > bool
            > list
            > conjuntos
            > tuple
            > dict
        - Profundizado en Listas y Diccionarios
        - Operadores
            > Operadores aritméticos
            > Operadores de asignación
            > Operadores de comparación
            > Operadores lógicos
        - Condicionales (y anidados)
        - Ciclos
            > While
            > For
        - Funciones (y métodos)
    2. Nivel Medio de Python
        - Lectura y Escritura de Archivos
        - Módulos y librerías (y pip)
            > os
            > math (y random)
            > time (y datetime)
            > tkinter
            > csv y json
            > pickle (y dill)
            > bs4 y requests
            > matplotlib
            > numpy
            > pandas
            > pyttsx3
            > speech_recognition
            > webbrowser
            > OpenCV
            > socket
        - Bases de datos
            > SQLite
            > MySQL
    3. Nivel Avanzado de Python
        - Clases (y programación orientada a objetos)
        - Hilos (Threads)
        - Excepciones
        - Regex
    4. Ejemplos, ejercicios...
        - Explicación de la metodología recomedada
        - Ejercicio 1: Asistente por comandos (programa de consola)
        - Ejercicio 2: Calculadora (GUI Graphical User Interface)
        - Ejercicio 3: Graficadora de funciones
        - Ejercicio 4: Webscraper
        - Ejercicio 5: Programando un juego en PyGame
        - Ejercicio 7: Habla artificial
        - Ejercicio 8: Reconocimiento de voz
        - Ejercicio 9: Análisis de imágenes con OpenCV
        - Ejercicio 10: Servidor local con socket
'''

# ####### 1. Básico de Python #############################

# 1.1 ¿Qué es Python?
'''
Python es un lenguaje de programación de alto nivel (sentencias 
semejantes al lenguaje oral) interpretado (requiere de un intérprete)
y por lo general orientado a objetos.
El intérprete (https://www.python.org/downloads/) lee de arriba 
a abajo de izquierda a derecha.

Existen (por lo que a nosotros por ahora nos interesa) dos
tipos de programas:
    - Programas de consola: Se ejecutan (decimos que "corren") en
        la consola de comandos (cmd).
    - Programas de GUI: Se ejecutan en una ventana de interfaz y
        son a los que comúnmente estamos acostumbrados a usar.

Python tiene una sintaxis que diferencia entre mayúsculas y minúsculas.
y tiene en cuenta las indentaciones (tabulaciones). Por ejemplo,
no es lo mismo escribir:
    Print("Hola mundo")
que:
print("Hola mundo")
'''

# 1.2 Comentarios
'''
Los comentarios son anotaciones que dejamos en el código y que
el intérprete no lee. Pueden ser de varios tipos:
    - Comentarios de una sola línea: Se escriben empezando la línea con un #
    - Comentarios de múltiples líneas: Se escriben entre comillas 
        triples (las que empiezan y acaban este comentario).
'''

# 1.3 Comando print()
'''
El comando print() es una función que imprime un dato en la consola.
Su sintaxis es:
print(dato)
Ejemplo:
print("Hola mundo")
'''

# 1.4 Variables y tipos de datos
'''
Las variables son espacios en la memoria RAM que almacenan un dato
que nosotros le ordenamos que almacene, asignándole un "nombre".
Cuando queremos acceder al dato usamos ese nombre.

Existen varios tipos de datos:
    - int: Números enteros
    - float: Números decimales
    - complex: Números complejos
    - str: Cadenas de caracteres. Van siempre entre comillas 
        (dobles o simples, da igual): "Hola mundo" o 'Hola mundo'
    - bool: Valores booleanos, es decir, True o False (Verdadero o Falso),
        se usan para representar valores que solo pueden tomar dos estados.
    - list: Listas, es decir, conjuntos de datos que se ordenan en una
        secuencia.
    - tuple: Las tuplas son listas pero que no se pueden modificar
        una vez creadas.
    - set: Conjunto de datos únicos (sin duplicados).
    - dict: Diccionarios, es decir, conjuntos de datos a los que dentro
        del mismo conjunto se le asigna un nombre a cada sub-valor.

Para darle un valor o crear una variable se escribe lo siguiente:

nombre_variable = valor_variable

para convertir un valor de un tipo de dato a otro se escribe:

tipo_de_dato(valor)

Como ejemplo de todo esto:

subscriptores_del_canal = float(381)

Así tendríamos una variable llamada subscriptores_del_canal que
almacena un valor decimal de 381.0, si quisiéramos cambiarlo a un
entero, podemos hacerlo así:

subscriptores_del_canal = int(subscriptores_del_canal)

Para eliminar una variable se escribe:

del nombre_variable
'''

# 1.5 Profundizado en Listas, tuplas, conjuntos y Diccionarios

# 1.5.1 Listas
'''
Las listas se declaran con corchetes:

lista = [1, 2, 3, 4, 5]

Pueden ser de cualquier tipo de dato, de otras listas e incluso
mezclar tipos de datos:

lista = [1, "Hola", True, [1, 2, 3]]

Para acceder a un elemento de la lista se pone la lista y el índice
del elemento que queremos entre corchetes:

lista[índice]

Los índices empiezan en 0, por lo que el primer elemento de 
la lista es lista[0] y también se pueden poner índices negativos
para referirnos a elementos de la lista desde el final; así
lista[-1] es el último elemento de la lista.
'''

# 1.5.2 Tuplas
'''
Con las tuplas es todo igual a como se hace con las listas (por ahora)
excepto que las tuplas no se pueden modificar y se declaran con
paréntesis:

tupla = (1, 2, 3, 4, 5)
'''

# 1.5.3 Conjuntos
'''
Los conjuntos se declaran con llaves:

conjunto = {1, 2, 3, 4, 5}

No son subscriptibles, es decir, no puedes poner:

conjunto[0]  # Esto da error

Pero sí son iterables y les puedes aplicar bucles como veremos
más adelante.

Son el resultado también de aplicar la función set() a un iterable,
retornando esta un conjunto sin duplicados de los componentes
del iterable.
'''

# 1.5.4 Diccionarios
'''
Los diccionarios se declaran con llaves:

diccionario = {
    "clave1": valor1,
    "clave2": valor2,
    ...
}
# Se diferencian de los conjuntos porque tienen claves y valores

Para acceder a un valor del diccionario se pone el dictionario y
la clave entre corchetes:

diccionario["clave"]
'''

# 1.6 Operadores
'''
Los operadores son unos signos que nos permiten realizar operaciones
entre valores. Existen varios tipos de operadores:
'''

# 1.6.1 Operadores aritméticos
'''
                Operador       Descripción
Suma:              +            Suma dos valores (números, strings, listas)
Resta:             -            Resta dos valores
Multiplicación:    *            Multiplica dos valores
División:          /            Divide dos valores
División entera:   //           Divide dos valores y devuelve un entero
Módulo:            %            Obtiene el resto de una división
Exponenciación:    **           Potencia de un valor
'''

# 1.6.2 Operadores de asignación
'''
                             Operador       Descripción
Asignación:                     =           Asigna un valor a una variable
Asignación de suma:            +=           Suma un valor a una variable
Asignación de resta:           -=           Resta un valor a una variable
Asignación de multiplicación:  *=           Multiplica un valor a una variable
Asignación de división:        /=           Divide un valor a una variable
Asignación de división entera: //=          Divide un valor a una variable y devuelve un entero
Asignación de módulo:          %=           Obtiene el resto de una división
Asignación de exponenciación:  **=          Potencia de un valor

Ejemplo:

subscriptores_del_canal = 381
subscriptores_del_canal += 1

Ahora subscriptores_del_canal vale 382
'''

# 1.6.3 Operadores de comparación
'''
                        Operador       Descripción
Igualdad:                  ==           Devuelve True si son iguales
Desigualdad:               !=           Devuelve True si son distintos
Menor que:                 <            Devuelve True si el primero es menor que el segundo
Menor o igual que:         <=           Devuelve True si el primero es menor o igual que el segundo
Mayor que:                 >            Devuelve True si el primero es mayor que el segundo
Mayor o igual que:         >=           Devuelve True si el primero es mayor o igual que el segundo
Dentro de un iterable:     in           Devuelve True si el valor está dentro del iterable

Ejemplo:

2 in [1, 2, 3, 4]  # (True)
3 in range(1, 20)  # (True)

!!Anotacion: range(x, y) devuelve un iterable de 
valores desde x hasta y incluyendo "x" y excluyendo "y".
En caso de escribir range(x) se devolvería lo mismo
que en range(0, x)
'''

# 1.6.4 Operadores lógicos
'''
            Operador       Descripción
Y:            and           Devuelve True si ambos valores son True
O:            or            Devuelve True si algún valor es True
No:           not           Devuelve True si el valor es False
'''

# 1.7 Condicionales
'''
Los condicionales se usan para decidir en función de un valor
si se ejecuta una parte de código o no.
Tenemos el if, el elif y el else. El if es el que se ejecuta si
el valor de la condición es True, el elif es el que se ejecuta si
el valor de la primera condición es False y la segunda es True, y
el else es el que se ejecuta si ambas condiciones son False.
Se pueden escribir cuantos elif se quiera:

if condición:
    código
elif condición:
    código
...
else:
    código
'''

# 1.8 Ciclos
'''
Los ciclos se usan para repetir una acción un número de veces.
Existen dos tipos principales de ciclos:
'''

# 1.8.1 Ciclo while
'''
El ciclo while se usa para repetir una acción mientras una 
condición es True.
Se escribe de la siguiente manera:

while condición:
    código

Se puede cortar el ciclo si dentro del código se encuentra una
instrucción break.
Por ejemplo podría ser:

while condición:
    código
    if condición2:
        break
'''

# 1.8.2 Ciclo for
'''
El ciclo for se usa para iterar sobre una lista, cadena... O cualquier
dato iterable.
Se escribe de la siguiente manera:

for elemento in lista:
    código

En este código, si usamos la variable "elemento" accedemos al valor
de cada elemento de la lista a lo largo de las iteraciones.
También se puede usar la variable "índice" para contar todos los
números enteros en un rango, como en el siguiente ejemplo:

for i in range(0, 10):
    código

donde i va de 0 a 9.
'''

# 1.9 Funciones y Métodos

# 1.9.1 Funciones
'''
Las funciones son bloques de código a los que se le asigna un
nombre y que se pueden llamar desde cualquier parte del código.
Se usan para no repetir grandes cantidades de código, para
separar una parte del código de otra y para hacer el código más
comprensible.
Se definen de la siguiente manera:

def nombre_de_la_función(argumento1, argumento2, ..., argumento_voluntario=valor_por_defecto):
    código
    return valor

Donde los argumentos son valores que se le pasan a la función
cuando se la llama y por tanto dependen del momento en el que
se llama.
El return es para devolver un valor de la función. En caso de no
añadir return se devuelve None.
Para llamar a la función se escribe de la siguiente manera:

nombre_de_la_función(argumento1, argumento2, ...)

Y si se quiere capatar el valor que devuelve de la función se haría
así:

nombre_de_una_variable = nombre_de_la_función(argumento1, argumento2, ...)
'''

# 1.9.2 Métodos
'''
Los métodos son funciones que pertenecen a un objeto (por ahora 
tipo de dato). Cada clase (por ahora tipo de dato), tiene sus
métodos propios que aplican efectos involucrando a la propia clase.

Cómo declararlos lo veremos en el apartado de clases.

Para ver los métodos de los tipos de datos que vimos hasta ahora
podéis visitar la documentación:
    - https://docs.python.org/es/3/library/string.html
    - https://docs.python.org/es/3/tutorial/datastructures.html
'''


# ###### 2. Nivel Medio de Python #########################

# 2.1 Lectura y escritura de archivos
'''
Para la lectura y escritura de archivos se usa el comando open.
Su sintaxis es la siguiente:

file = open(nombre_del_archivo, modo)
...
file.close()

Donde el modo va en función de lo que se quiera hacer con el archivo:
    - 'r': Lectura de texto
    - 'w': Escritura de texto
    - 'a': Escritura de texto añadiendo al final del archivo
    - 'rb': Lectura de binario
    - 'wb': Escritura de binario
    - 'ab': Escritura de binario añadiendo al final del archivo
File, (antes del close) nos servirá para acceder a la información 
del archivo. Su sintaxis es la siguiente:

variable = file.read()       # Esto lee todo el archivo
variable = file.readlines()  # Esto lee todas las líneas del archivo (y las guarda en una lista)
file.write(texto)            # Esto escribe texto en el archivo
file.writelines(lista)       # Esto escribe una lista de líneas de texto en el archivo
'''

# 2.2 Módulos y librerías (y pip)
'''
Los módulos y librerías son archivos que contienen código de 
otra persona y que puedes utilizar para tus programas sin necesidad
de copiarlo a tus archivos.
Algunos vienen instalados por defecto cuando se instala Python,
pero otras hay que descargarlas. Para eso usaremos pip.

Para instalar una librería, nos dirigimos a la terminal o cmd y
escribimos:

    pip install nombre_de_la_librería

(o en caso de tener varias versiones de Python):

    pip3 install nombre_de_la_librería

Para cotejar qué versión de Pip estás usando escribes:

    pip --version (o pip3 --version)

Para cotejar qué librerías tienes instaladas escribes:

    pip freeze (o pip3 freeze)


Para usar una librería, se debe importarla. Para ello usaremos
la palabra reservada import:

import nombre_de_la_librería

o si queremos importar un objeto, función... en concreto de 
una librería escribimos:

from nombre_de_la_librería import nombre_del_objeto

En caso de querer importar todos los objetos de una librería
escribimos:

from nombre_de_la_librería import *

Y en caso de querer importar de una subcarpeta de una librería:

from nombre_de_la_librería.subcarpeta import nombre_del_objeto

O en caso de querer importar una librería o subcarpeta asignándole
un nombre de variable:

import nombre_de_la_librería as nombre_de_la_variable
(o)
import nombre_de_la_librería.subcarpeta as nombre_de_la_variable

Existen muchísimas, ahora vamos a ver algunas de las más comunes:
'''

# 2.2.1 os
'''
os es una librería que nos permite acceder a funciones
del sistema operativo.

import os

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

os.getcwd()                # Devuelve el directorio de trabajo actual
os.chdir(path)             # Cambia el directorio de trabajo a path
os.mkdir(path)             # Crea un directorio en path
os.rmdir(path)             # Elimina el directorio path
os.remove(path)            # Elimina el archivo path
os.rename(path1, path2)    # Renombra el archivo path1 a path2
os.path.join(path1, path2) # Devuelve la ruta unión de path1 y path2 (se usa principalmente para concatenar directorios con archivos)
os.path.exists(path)       # Devuelve True si el path existe
os.path.isfile(path)       # Devuelve True si path es un archivo
os.system(command)         # Ejecuta un comando en la terminal o cmd
os.popen(command)          # Ejecuta un comando en la terminal o cmd y devuelve un objeto que permite leer la salida
os.environ                 # Es un diccionario con todas las variables de entorno (y si editas el diccionario editas las variables...)
'''

# 2.2.2 math (y random)
'''
Math es una librería que nos permite usar funciones matemáticas.

import math

Tiene muchas constantes útiles, como:

math.pi
math.tau
math.e
math.inf

También funciones interesantes, algunas de las más usadas 
(por mí) son:

math.ceil(x)              # Devuelve el entero más cercano a x
math.floor(x)             # Devuelve el entero más cercano por debajo a x
math.factorial(x)         # Devuelve el factorial de x
math.log(x, y)            # Devuelve el logaritmo de x en base y


Random es una librería que nos permite generar números aleatorios.

import random

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

random.randint(a, b)      # Devuelve un entero aleatorio entre a y b
random.random()           # Devuelve un número aleatorio entre 0 y 1
random.choice(lista)      # Devuelve un elemento aleatorio de la lista
random.shuffle(lista)     # Mezcla la lista
'''

# 2.2.3 time (y datetime)
'''
time es una librería para el manejo de tiempo.

import time

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

time.sleep(x)       # Espera x segundos
time.strftime(fmt)  # Devuelve la fecha y hora actual en el formato indicado como string

datetime es una librería para el manejo de fechas y horas.

import datetime

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

datetime.datetime.now()      # Devuelve la fecha y hora actual
datetime.datetime.utcnow()   # Devuelve la fecha y hora actual en UTC
'''

# 2.2.4 tkinter
'''
tkinter es una librería para el manejo de interfaces gráficas.
Nos permite crear ventanas, botones, entradas de texto, etc...

import tkinter

La ventana principal es un objeto de clase tkinter.Tk()
y tienes múltiples métodos como Tk().title(), Tk().geometry(), etc.

window = tkinter.Tk()
window.title("Título de la ventana")

Para añadir elementos a la ventana, los definimos entre las
muchas clases de tkinter:

entrada_de_texto = tkinter.Entry(window, width=20, font="Arial 20")
boton = tkinter.Button(window, text="Hola Mundo", font="Arial 20", command=lambda: print("Hola Mundo"))

Para que se muestren en la ventana, los añadimos a la ventana
usando el método grid(), que los posiciona por filas y columnas:

entrada_de_texto.grid(row=0, column=0)
boton.grid(row=0, column=1)

Finalmente tras la edición de la ventana, hay que llamar al método
mainloop() para que se muestre:

window.mainloop()
'''

# 2.2.5 csv y json
'''
csv es una librería para el manejo de archivos CSV, usados por
ejemplo, en muchos datasets.

import csv

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

csv.reader(fichero_abierto_en_modo_r)        # Devuelve un objeto que permite leer el fichero
csv.writer(fichero_abierto_en_modo_w)        # Devuelve un objeto que permite escribir en el fichero

json es una librería para el manejo de archivos JSON, usados por
ejemplo, en muchas configuraciones.

import json

Tiene muchas funciones interesantes, algunas de las más usadas
(por mí) son:

json.load(fichero_abierto_en_modo_r)                 # Devuelve un diccionario con los datos del fichero
json.dump(diccionario, fichero_abierto_en_modo_w)    # Escribe en el fichero el diccionario
json.loads(string)                                   # Devuelve un diccionario con los datos del string en formato json
json.dumps(diccionario)                              # Devuelve un string en formato json con los datos del diccionario
'''

# 2.2.6 pickle (y dill)
'''
pickle es una librería para el manejo de archivos pickle, usados
para guardar objetos de python directamente en ficheros. Su 
problema es que referencia el origen por lo que no es portable de 
un proyecto a otro.

import pickle

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

pickle.dump(objeto, fichero_abierto_en_modo_w)   # Escribe en el fichero el objeto
pickle.load(fichero_abierto_en_modo_r)           # Devuelve el objeto guardado en el fichero

Normalmente se crea una función para escribir los ficheros:

def guardar_objeto(objeto, nombre_fichero):
    with open(nombre_fichero, 'wb') as f:
        pickle.dump(objeto, f)


Dill hace lo mismo, pero es portable de un proyecto a otro ya que
serializa los objetos directamente, sin referencias.

import dill

Los métodos que nos interesan son exactamente los mismos que en 
pickle. Tanto es así que podríamos hacer:

import dill as pickle

Y usarlo tal cual.
'''

# 2.2.7 bs4, urllib y requests
'''
urllib es una librería para el manejo de urls.

import urllib

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

urllib.request.urlopen(url)                 # Devuelve un objeto que permite leer el fichero
urllib.request.urlretrieve(url, fichero)    # Descarga el fichero


bs4 es una librería para el manejo de HTML y XML, y que se usa
principalmente en el scraping de páginas web.

import bs4

Su principal aportación es la clase BeautifulSoup

variable = BeautifulSoup(site)  # Donde site es un request.urlopen(url)
(o también puedes hacer)
variable = BeautifulSoup(html_code, 'html.parser')  # Para crearlo desde el código HTML

Tiene muchos métodos interesantes, algunos de los más usados 
(por mí) son:

variable.find_all(tag, attrs)            # Donde attrs es opcional y es un diccionario con los atributos. Devuelve una lista con todos los elementos tag
variable.find(tag, attrs)                # Donde attrs es opcional y es un diccionario con los atributos. Devuelve el primer elemento tag
variable.findAll(text=regex)             # Donde regex es una expresión regular. Devuelve una lista con todos los elementos que contengan el texto indicado

Cada una de las tags que retorna, tienen atributos, a los que
puedes acceder como:

tag['atributo']


requests es una librería para el manejo de peticiones HTTP. Se 
usa principalmente para descargar ficheros y webscraping.

import requests

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

requests.get(url)                 # Devuelve un objeto request.Response de la url
requests.post(url, data=datos)    # Envía una petición POST con los datos indicados
'''

# 2.2.8 matplotlib
'''
matplotlib es una librería para el manejo de gráficos.

import matplotlib.pyplot as plt

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

plt.plot(x, y)                # Dibuja una gráfica de "y" en función de "x"
plt.xlabel(texto)             # Pone el texto en el eje x
plt.ylabel(texto)             # Pone el texto en el eje y
plt.title(texto)              # Pone el texto en el título
plt.legend(texto)             # Pone el texto en la leyenda
plt.show()                    # Muestra la gráfica
plt.savefig(fichero)          # Guarda la gráfica en el fichero indicado
plt.close()                   # Cierra la gráfica
'''

# 2.2.9 numpy
'''
numpy es una de las librerías más usadas de python. Tiene grandes
implicaciones en el manejo de datos, inteligencia artificial...

numpy es una librería para el manejo de matrices uni y 
multidimensionales y vectores.

import numpy as np

Tiene muchas funciones interesantes, algunas de las más básicas,
de estar más interesado, puedes consultar la documentación:

np.array(lista)          # Devuelve una matriz de numpy con los elementos de la lista
np.array(lista, dtype)   # Devuelve una matriz de numpy con los elementos de la lista y el tipo de datos indicado
np.zeros(shape)          # Devuelve una matriz de numpy con todos los elementos a 0
np.ones(shape)           # Devuelve una matriz de numpy con todos los elementos a 1
np.linspace(a, b, n)     # Devuelve una matriz de numpy con n elementos entre a y b
np.arange(a, b, n)       # Devuelve una matriz de numpy con n elementos entre a y b
np.random.rand(shape)    # Devuelve una matriz de numpy con números aleatorios
np.random.randint(a, b, shape) # Devuelve una matriz de numpy con números aleatorios entre a y b
np.random.randn(shape)   # Devuelve una matriz de numpy con números aleatorios con distribución normal
np.random.choice(lista, n) # Devuelve una matriz de numpy con n elementos de la lista
np.random.shuffle(lista)  # Desordena la matriz de numpy
np.random.permutation(lista) # Devuelve una matriz de numpy con una permutación de la lista
np.where(condicion, a, b) # Devuelve una matriz con los elementos de a donde se cumple la condición de b donde no
'''

# 2.2.10 pandas
'''
pandas es una librería para el manejo de datos.

import pandas as pd

Tiene muchas funciones interesantes, algunas de las más usadas 
(por mí) son:

pd.read_csv(nombre_del_fichero)                   # Lee un fichero csv y lo devuelve como un DataFrame
pd.read_excel(nombre_del_fichero)                 # Lee un fichero excel y lo devuelve como un DataFrame
pd.read_json(nombre_del_fichero)                  # Lee un fichero json y lo devuelve como un DataFrame
pd.read_html(nombre_del_fichero)                  # Lee un fichero html y lo devuelve como una lista de DataFrames
pd.read_pickle(nombre_del_fichero)                # Lee un fichero pickle y lo devuelve como un DataFrame
pd.read_sql(sql, conexion)                        # Lee una consulta SQL y la devuelve como un DataFrame
pd.read_hdf(nombre_del_fichero)                   # Lee un fichero hdf y lo devuelve como un DataFrame
pd.read_excel(nombre_del_fichero, engine="odf")   # Lee un fichero OpenDocument Spreadsheets y lo devuelve como un DataFrame

También provee la clase DataFrame, que almacena información y
posee los siguientes métodos:

DataFrame.to_csv(nombre_del_fichero)                   # Guarda el DataFrame en un fichero csv
DataFrame.to_excel(nombre_del_fichero)                 # Guarda el DataFrame en un fichero excel
DataFrame.to_json(nombre_del_fichero)                  # Guarda el DataFrame en un fichero json
DataFrame.to_pickle(nombre_del_fichero)                # Guarda el DataFrame en un fichero pickle
DataFrame.to_sql(nombre_tabla, conexion)               # Guarda el DataFrame en una tabla en una base de datos
DataFrame.to_hdf(nombre_del_fichero)                   # Guarda el DataFrame en un fichero hdf
DataFrame.to_excel(nombre_del_fichero, engine="odf")   # Guarda el DataFrame en un fichero OpenDocument Spreadsheets
DataFrame.to_latex(nombre_del_fichero)                 # Guarda el DataFrame en un fichero latex
DataFrame.to_dict(orient="index")                      # Devuelve un diccionario con los datos del DataFrame
DataFrame.values                                       # Devuelve una matriz numpy con los datos del DataFrame
DataFrame.columns                                      # Devuelve una lista con los nombres de las columnas

Y también se puede acceder a los datos por columnas o por filas:

DataFrame[columna].values    # Devuelve una matriz numpy con los datos de la columna
DataFrame.loc[fila].values   # Devuelve una matriz numpy con los datos de la fila
'''

# 2.2.11 pyttsx3
'''
pyttsx3 es una librería para el manejo de texto hablado. Nos
permite que el ordenador lea un texto en voz alta.

import pyttsx3

Primero se debe instanciar el objeto, el cual tendrá métodos
como por ejemplo setProperty para fijar características de la voz:

engine = pyttsx3.init()
engine.setProperty('rate', 130)

Cuando queremos leer un texto, lo normal es crear una función
sayText que lo haga:

def sayText(text):
    engine.say(text)
    engine.runAndWait()
'''

# 2.2.12 speech_recognition
'''
speech_recognition es una librería para el manejo de 
reconocimiento de voz.

import speech_recognition as sr

Lo primero que hay que hacer es crear un objeto de la clase
Recognizer, que nos permite reconocer el texto que hablamos:

r = sr.Recognizer()

Para reconocer texto, en el audio gravado por el micrófono:

with sr.Microphone() as source:
    audio = r.listen(source)
    texto = r.recognize_google(audio, language="lenguaje")

Para reconocer texto desde un fichero de audio:

with sr.AudioFile(nombre_del_fichero) as source:
    texto = r.recognize_google(source, language="lenguaje")
'''

# 2.2.13 OpenCV
'''
OpenCV es una librería para el manejo de imágenes. Nos permite
implementar funciones de búsqueda de contornos, detección de
objetos y bordes, etc...

import cv2

En relación a imágenes en el disco duro:

img = cv2.imread(nombre_de_la_imagen)  # Lee una imagen
cv2.imwrite(nombre_del_fichero, img)   # Guarda una imagen

Otra de las características de OpenCV es el tratado de
vídeos como secuencias de imágenes. Para leer un vídeo en el
disco duro:

cap = cv2.VideoCapture(nombre_del_fichero)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # ret es un booleano que indica si se ha leído una imagen
    # frame es la imagen leída

Muy importante que tras leer todo, cerremos el objeto:

cap.release()

OpenCV nos provee una gran cantidad de filtros y funciones
diferentes para tratar imágenes.

Otra característica de OpenCV es la capacidad de tomar
imágenes y vídeos desde la cámara del ordenador.
Para imágenes:

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

Para vídeos:

cap = cv2.VideoCapture(0)

Ahora hacemos un bucle que lee imágenes en secuencia, valdría
cualquiera de los vistos a lo largo del curso, depende del fin
que se busque, por ejemplo:

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

En caso de querer guardarlo en un fichero, debemos instanciar
un objeto de la clase VideoWriter y escribirlo con el:

out = cv2.VideoWriter(nombre_del_fichero, cv2.VideoWriter_fourcc(*'XVID'), fps, resolucion)

Y para cada frame que se lea, escribirlo:

out.write(frame)

Como siempre muy importante, cerramos los objetos:

cap.release()
out.release()
'''

# 2.2.14 socket
'''
socket es una librería para el manejo de conexiones. Nos permite
crear conexiones de intercambio de datos a partir de una dirección
IP y puertos.

import socket

Es complejo de usar pero muy útil, por lo que recomiendo mucho 
leer la documentación de la librería y hacer el último 
ejercicio del curso. En general:

    - Crear un objeto de la clase socket:

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    - Conectar el objeto a una dirección IP y un puerto:

s.connect((ip, puerto))

    - Enviar datos:

s.sendall(bytes_de_lo_que_quieres_enviar)

    - Recibir datos:

data = b''
while True:
    recvfile = s.recv(4096)
    if recvfile == mensaje_específico_del_servidor_para_cierre_de_mensajes_en_forma_de_bytes:
        break
    data = recvfile + data
# Esto lee los bytes enviados y los guarda como bytes en la 
# variable data

    - Crear un socket para escuchar conexiones:

s.listen(numero_de_conexiones_a_escuchar)
conn, addr = s.accept()
whith conn:
    # usar conn para enviar y recibir datos con los mismos 
    # métodos que en el socket de conexión
'''

# 2.3 Bases de datos
'''
Las bases de datos se usan para almacenar información de manera 
que no se borren tras el apagado.
Existen dos tipos de bases de datos:
    - SQL Server: Base de datos estilo servidor.
    - SQLite: Base de datos en archivo.
Para trabajar con cualquiera de ellas es necesario conocer la
sintaxis de los comandos SQL. Tendremos un curso sobre esta en
el canal próximamente pero así de forma rápida:

SELECT * FROM nombre_de_la_tabla;                                                                                                          Esto devuelve todos los registros de la tabla
SELECT * FROM nombre_de_la_tabla WHERE condición;                                                                                          Esto devuelve los registros que cumplen la condición
CREATE TABLE "nombre_de_la_tabla" ("nombre_de_un_campo" TIPO_DE_DATO MATICES,...);                                                         Esto crea una tabla con los campos indicados
INSERT INTO "nombre_de_la_tabla" ("nombre_de_un_campo", "nombre_de_un_campo", ...) VALUES ("valor", "valor", ...);                         Esto inserta un registro en la tabla
UPDATE "nombre_de_la_tabla" SET "nombre_de_un_campo" = "valor", "nombre_de_un_campo" = "valor", ... WHERE "nombre_de_un_campo" = "valor";  Esto actualiza un registro en la tabla
DELETE FROM "nombre_de_la_tabla" WHERE "nombre_de_un_campo" = "valor";                                                                     Esto borra un registro de la tabla
DROP TABLE "nombre_de_la_tabla";                                                                                                           Esto borra una tabla

Normalmente, yo uso SQLite para trabajar con mi base de datos
dado que para aplicaciones medianas es normalmente más práctico.
Aun así, vamos a ver ambas opciones.
'''

# 2.3.1 SQLite
'''
Para trabajar con SQLite se usa el módulo sqlite3.
Normalmente se crea una función que ejeuta los comandos SQL
que nosotros ordenamos:

import sqlite3
def run_query(db_name, query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

Donde db_name es el nombre del archivo de la base de datos, query
es el comando SQL que queremos ejecutar y parameters es una lista
de los parámetros que necesitamos para ejecutar el comando (valores
que substituimos en la query como ?).
Así cuando queremos ejecutar, por ejemplo, un SELECT, podemos hacer:

result = run_query('database.db', 'SELECT * FROM table_name')
'''

# 2.3.2 SQL
'''
Para trabajar con SQL se usa el módulo pyodbc y pandas:

import pyodbc 
import pandas as pd
server = 'server_name, port_number' 
database = 'database_name' 
username = 'username' 
password = 'password' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

Para ejecutar un comando SQL, podemos hacer:

result = pd.read_sql_query('SELECT * FROM table_name', conn)

result ahora es un DataFrame de pandas.
Por último, debemos cerrar la conexión:

conn.close()
'''


# ###### 3. Nivel Avanzado de Python #########################

# 3.1 Clases
'''
Las clases son una forma de organizar nuestras aplicaciones.
Python está orientado a objetos, es decir, crear clases que 
asignamos a objectos reales para registrar sus propiedades.

Para declarar una clase, se usa la siguiente sintaxis:

class NombreDeLaClase:
    atributos_de_la_clase

Los atributos de la clase son sus "propiedades", sus variables
internas y sus métodos.
Se usa para todo ello la palabra reservada "self" para acceder
a otras propiedades.

Para declarar métodos, se usa la siguiente sintaxis:

class NombreDeLaClase:
    def nombre_del_método(self, parámetros):
        código_del_método

Hay un método que se declara prácticamente siempre, el constructor.
El constructor es el método que se ejecuta cuando se crea una
nueva instancia de la clase. Se declara así:

class NombreDeLaClase:
    def __init__(self, parámetros):
        código_del_constructor

Los atributos de la clase se declaran dentro del constructor
o después del "class NombreDeLaClase:" de la siguiente forma:

self.nombre_del_atributo = valor_del_atributo

Una variable interna que se suele usar para ahorrar espacio de
memoria es __slots__, la cual es una lista de los atributos de la
clase. Se declara después de la línea "class NombreDeLaClase:".

Para acceder a otros métodos o atributos desde un método, se usa
self también. Por ejemplo:

class Persona:
    __slots__ = ['nombre', 'apellido', 'edad']
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def get_data(self):
        return [self.nombre, self.apellido, self.edad]
'''

# 3.1.1 Herencia
'''
Una clase puede heredar atributos y métodos de otra clase.
Una herencia se declara así:

class NombreDeLaClase(NombreDeLaClasePadre):
    atributos_de_la_clase

De esta forma, se puede acceder a los atributos y métodos de la
clase padre, usando la palabra reservada "super".

class Animal:
    __slots__ = ['tipo', 'esperanza_de_vida']
    def __init__(self, tipo, esperanza_de_vida):
        self.tipo = tipo
        self.esperanza_de_vida = esperanza_de_vida

class Persona(Animal):
    __slots__ = ['nombre', 'apellido', 'edad']
    def __init__(self, nombre, apellido, edad):
        super().__init__('Person', 90)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def get_data(self):
        return [self.nombre, self.apellido, self.edad, self.tipo, self.esperanza_de_vida]
'''

# 3.2 Threads
'''
Los hilos son una forma de ejecutar código en paralelo, es decir,
simultáneamente.
Para trabajar con hilos, se usa el módulo threading.
Se usa así:

import threading
def funcion(parametros):
    código_de_la_función
thread = threading.Thread(target=funcion, args=(parametros,))
thread.start()

Para volver a juntar el hilo al principal, se usa el método join():

thread.join()

Una manera que proponemos de acostumbrarse a los hilos es
importar el módulo time y usarlo para ver las diferencias de tiempo
modificando el código con hilos.
'''

# 3.3 Excepciones
'''
Las excepciones son una forma de controlar errores en el código.
Los errores no solo se dan cuando hay fallos en el código, sino
que también pueden ser causados por otros factores externos.

Las excepciones sirven para decir qué hacer cuando se produce un
error.
Su sintaxis es la siguiente:

try:
    código_que_puede_fallar
except NombreDelError:
    código_a_ejecutar_cuando_se_produzca_la_excepción

Si quisiéramos prevenir TODOS los errores, escribiríamos el siguiente
código:

try:
    código_que_puede_fallar
except:
    código_a_ejecutar_cuando_se_produzca_la_excepción
'''

# 3.4 Regex (Regular Expressions)
'''
Las RegEx son una forma de buscar patrones en cadenas de texto.
Para trabajar con ellas, se usa el módulo re.
Su sintaxis es la siguiente:

import re
cadena = 'cadena de texto'

Ahí tenemos un escenario, en el que queremos usar re para buscar
patronse en una cadena de texto. Para ello, existen diversos métodos:

resultado = re.search(patron, cadena)          # Retorna el primer resultado en forma de objeto de tipo Match
resultado = re.findall(patron, cadena)         # Retorna una lista con todos los resultados en formato string
resultado = re.finditer(patron, cadena)        # Retorna una lista con todos los resultados en formato objeto de tipo Match
resultado = re.sub(patron, reemplazo, cadena)  # Retorna la cadena con los reemplazos hechos

La sintaxis de expresiones regulares es muy variada, pero aquí
dejamos algunos elementos principales:

\d     Caracter numérico
\D     Caracter no numérico
\w     Caracter alfanumérico
\W     Caracter no alfanumérico
\s     Caracter espacio en blanco
\S     Caracter no espacio en blanco
.      Caracter cualquiera
[abc]  Caracter que esté en la lista
[^abc] Caracter que no esté en la lista
[a-z]  Caracter que esté entre a y z
[^a-z] Caracter que no esté entre a y z
*      Repite el caracter anterior 0 o mas veces
{a, b} Repite el caracter anterior entre a y b veces
a||b   Caracter que sea a o b
?      Tomar la mínima unidad de la expresión
+      Tomar la máxima unidad de la expresión

Ejemplo de expresiones regulares son:
[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,6}     # Email
\d{3}-\d{3}-\d{3}                     # Teléfono
\d{1,2}/\d{1,2}/\d{4}                 # Fecha
\d{1,2}:\d{2}(:\d{2})?                # Hora
'''

# #############################################################
# #############################################################
# #############################################################
# ########## 4. Ejemplos y ejercicios #########################
# #############################################################
# #############################################################
# #############################################################

# 4.1  Explicación de la metodología recomedada
'''
El método que vamos a recomendar para llevar estos ejercicios
es el siguiente:

Primero, les daremos la explicación del ejercicio (qué tienen que 
hacer). Acto seguido, sugerimos que tras leer y comprender el 
ejercicio, intenten hacerlo ustedes, en base a los contenidos que
hemos visto y buscando la documentación extra necesaria en las
documentaciones oficiales de las librerías o de Python.

Si tras intentarlo, no logran hacerlo, entonces pueden ver 
la solución que les dejaremos explicada en el ejercicio.
'''

# 4.2  Ejercicio 1: Asistente por comandos (programa de consola)
'''
EXPLICACIÓN:
El ejercicio consiste en crear un programa de consola que
solicite al usuario que ingrese un comando de terminal (o cmd) y
que lo ejecute.

PISTA (⚠ LEER SOLO SI NECESARIO):

Tendrán que usar la función input() junto al módulo os y 
la función system(comando).
'''

'''
SOLUCIÓN:

from os import system
from time import sleep

while True:
    comando = input('Ingrese un comando: ')
    if comando == 'exit':
        break
    system(comando)
    sleep(0.01)  # Evitar sobrecarga del CPU en un bucle infinito
'''

# 4.3  Ejercicio 2: Calculadora (GUI Graphical User Interface)
'''
EXPLICACIÓN:
El ejercicio consiste en crear una calculadora con interfaz
gráfica, es decir, con ventanas. El usuario podrá ingresar
una operación y el programa mostrará el resultado.

PISTA (⚠ LEER SOLO SI NECESARIO):

Tendrán que usar la librería tkinter, y puede que el módulo math,
lo último dependerá del tipo de cuentas que quiere que pueda 
realizar su calculadora.
'''

'''
SOLUCIÓN: (UNA UN POCO TRYHARD PERO BUENO)

en el archivo "ejercicios_resueltos/calculadora.py"
'''

# 4.4  Ejercicio 3: Graficadora de funciones
'''
EXPLICACION:
Este ejercicio consiste en crear una aplicacion que permita 
graficar funciones introducidas por el usuario.

PISTA (⚠ LEER SOLO SI NECESARIO):

Necesitará usar numpy, tkinter, matplotlib, math, y la función eval().
'''

'''
SOLUCIÓN:
en el archivo "ejercicios_resueltos/graficadora.py"
'''

# 4.5  Ejercicio 4: Webscraper
'''
EXPLICACION:
Este ejercicio consiste en crear una aplicación que scrapee
datos de una página web a nivel de SEO. Obtendrá la url real
(si tiene o no https, www, etc), el título, las meta tags,
los links, etc... Un poco sacar los datos que influyen en el
SEO.

PISTA (⚠ LEER SOLO SI NECESARIO):

Necesitará usar urllib, BeautifulSoup, y puede que el módulo re.
'''

'''
SOLUCIÓN: 
en el archivo "ejercicios_resueltos/webscraper.py"
'''

# 4.6  Ejercicio 5: Programando un juego en PyGame
# ⚠ PyGame es un módulo que no hemos trabajado en este documento,
# podéis consultarla en la documentación oficial de PyGame o en
# el video sobre creación de un juego en PyGame qu hay en el canal.
'''
EXPLICACION:
Este ejercicio consiste en crear un juego básico con el 
módulo PyGame. El ejemplo consiste en un objeto que puedes mover
en el eje y y una bola. El objetivo será hacer el máximo de paradas
con el objeto con el mínimo de goles.

PISTA (⚠ LEER SOLO SI NECESARIO):

solo necesita usar PyGame.
'''

'''
Solución: 
en el archivo "ejercicios_resueltos/juego.zip"
'''

# 4.7  Ejercicio 6: Habla artificial
'''
EXPLICACION:
Este ejercicio consiste en crear una aplicación de interfaz que
permita al usuario introducir un texto y que lo lea por voz el
computador.

PISTA (⚠ LEER SOLO SI NECESARIO):
Necesitará usar la librería pyttsx3 o la librería gtts.
'''

'''
SOLUCIÓN: 
en el archivo "ejercicios_resueltos/habla_artificial.py"
'''

# 4.8  Ejercicio 7: Reconocimiento de voz
'''
EXPLICACION:
Este ejercicio consiste en crear una aplicación que permita al
usuario darle comandos por voz y este reaccione en consecuencia.
Por ejemplo: "Abre las noticias", "Abre el navegador", etc...

PISTA (⚠ LEER SOLO SI NECESARIO):
Necesitará usar la librería speech_recognition, webbrowser y comparaciones 
if-elif-...-else
'''

'''
SOLUCIÓN: 
en el archivo "ejercicios_resueltos/reconocimiento_voz.py"
'''

# 4.9  Ejercicio 8: Análisis de imágenes con OpenCV
'''
EXPLICACION:
Este ejercicio consiste en crear una aplicación que lea
un video, lo transforme a resolución 1280x720 y blurree 
las caras detectadas en las imágenes. Posteriormente, debe 
guardar el video en una dirección elegida por el usuario.

PISTA (⚠ LEER SOLO SI NECESARIO):
Necesitará usar la librería cv2, y la función cv2.VideoCapture(),
numpy, math y time junto a tkfilebrowser.
'''

'''
SOLUCIÓN:
en el archivo "ejercicios_resueltos/analisis_imagenes.py"
'''

# 4.10 Ejercicio 9: Servidor local con socket
'''
EXPLICACION:
Este ejercicio consiste en crear una aplicación que permita
la comunicación entre un cliente y un servidor que se encuentren
en la misma red wifi. Necesitarás crear dos aplicaciones:
una para el cliente y otra para el servidor.

PISTA (⚠ LEER SOLO SI NECESARIO):

Necesitará usar la librería socket y el módulo threading.
'''

'''
SOLUCIÓN:
Se encuentra en el archivo "servidor_local.zip"
    parte del cliente en el archivo "cliente.py"
    parte del servidor en el archivo "servidor.py"
'''