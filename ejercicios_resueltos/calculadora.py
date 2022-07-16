from tkinter import *
import random
import math
import webbrowser

# Creamos la ventana y la matizamos
ventana = Tk()
ventana.title("Calculadora")
ventana.configure(background="#FF0000")

# Creamos las entradas de texto y las añadimos a la ventana
e_texto = Entry(ventana, font=("Calibri 20"), background = "#7FFF00")
e_textoal1 = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_textoal2 = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")

e_texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
e_textoal1.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
e_textoal2.grid(row = 1, column = 3, columnspan = 2, padx = 5, pady = 5)

e_textoal1.insert(0,"comienzo del rango del rand")
e_textoal2.insert(0,"final del rango del rand")

e_logsubin = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_logbase = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_logbase.grid(row = 0, column = 6, columnspan = 2, padx = 5, pady = 5)
e_logsubin.grid(row = 0, column = 8, columnspan = 2, padx = 5, pady = 5)
e_potbas = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_potexp = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_potbas.grid(row = 1, column = 6, columnspan = 2, padx = 5, pady = 5)
e_potexp.grid(row = 1, column = 8, columnspan = 2, padx = 5, pady = 5)

e_percent1 = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_percent2 = Entry(ventana, font= ("Calibri 8"), background = "#7FFF00")
e_percent1.grid(row = 8, column = 6, columnspan = 2, padx = 5, pady = 5)
e_percent2.grid(row = 8, column = 9, columnspan = 2, padx = 5, pady = 5)
i = 0





# Creamos las funciones necesarias
def click_boton(valor):
    global i
    e_texto.insert(i, valor)  # Insertar el valor en la posición i de la entrada
    i += 1

def borrar():
    e_texto.delete(0, END)  # Borrar el contenido de la entrada
    i = 0


def factorial():
    prod=1
    numfact = math.ceil(float(e_texto.get()))  # Tomamos el número redondeado
    for i in range(1,numfact+1):  # Recorremos el rango del número
        prod=prod*i
    e_texto.delete(0, END)  # Eliminamos lo que había en la entrada
    e_texto.insert(0, prod)  # Insertamos el resultado

def hacer_operacion():
    operacion = e_texto.get()  # Obtenemos la operación
    resultado = eval(operacion)  # Usamos eval() para realizarla
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

def al():
    numeroal = random.randint(float(e_textoal1.get()), float(e_textoal2.get()))  # Obtenemos un número aleatorio entre el rango indicado
    e_texto.delete(0, END)
    e_texto.insert(0, numeroal)

def logaritmo():
    global e_logbase
    global e_logsubin
    e_texto.delete(0, END)
    e_texto.insert(0, math.log(int(math.trunc(float(e_logbase.get()))), int(math.trunc(float(e_logsubin.get())))))  # Insertamos el logaritmo

def potencia():
    e_texto.delete(0, END)
    e_texto.insert(0, float(e_potbas.get())**float(e_potexp.get()))

def raiz():
    raiz = math.sqrt(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, raiz)

def rad():
    rad1 = math.radians(float(e_texto.get()))  # Esta función convierte los grados a radianes
    e_texto.delete(0, END)
    e_texto.insert(0, rad1)

def grados():
    grad1 = math.degrees(float(e_texto.get()))  # Esta función convierte los radianes a grados
    e_texto.delete(0, END)
    e_texto.insert(0, grad1)

def cotangente():
    tan = math.tan(float(e_texto.get()))
    cotan = 1 / tan
    e_texto.delete(0, END)
    e_texto.insert(0, cotan)

def secante():
    cos = math.cos(float(e_texto.get()))
    sec = 1 / cos
    e_texto.delete(0, END)
    e_texto.insert(0, sec)


def cosecante():
    sin = math.sin(float(e_texto.get()))
    cosec = 1 / sin
    e_texto.delete(0, END)
    e_texto.insert(0, cosec)

def cotangenteh():
    tanh = math.tanh(float(e_texto.get()))
    cotan = 1 / tanh
    e_texto.delete(0, END)
    e_texto.insert(0, cotan)

def secanteh():
    cosh = math.cosh(float(e_texto.get()))
    sech = 1 / cosh
    e_texto.delete(0, END)
    e_texto.insert(0, sech)


def cosecanteh():
    sinh = math.sinh(float(e_texto.get()))
    cosech = 1 / sinh
    e_texto.delete(0, END)
    e_texto.insert(0, cosech)

def seno():
    sin = math.sin(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, sin)

def coseno():
    cos = math.cos(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, cos)

def tangente():
    tan = math.tan(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, tan)

def senh():
    sinh = math.sinh(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, sinh)

def cosh():
    cosnh = math.cosh(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, cosnh)

def tanh():
    tangh = math.tanh(float(e_texto.get()))
    e_texto.delete(0, END)
    e_texto.insert(0, tangh)

def porcentaje():
    porc = float(e_texto.get())
    unid = porc / 100
    e_texto.delete(0, END)
    e_texto.insert(0, unid)

def ln():
    enter = float(e_texto.get())
    ln1 = math.log(enter, math.e)  # El logaritmo neperiano es el logaritmo en base e
    e_texto.delete(0, END)
    e_texto.insert(0, ln1)

def ex():
    expo = float(e_texto.get())
    ex1 = math.e ** expo
    e_texto.delete(0, END)
    e_texto.insert(0, ex1)

def percent():
    percent1 = float(e_percent1.get())
    percent2 = float(e_percent2.get())
    percent3 = (percent1/100) * percent2
    e_texto.delete(0, END)
    e_texto.insert(0, percent3)

def der():
    url = 'https://es.symbolab.com/solver/derivative-calculator'
    webbrowser.open(url, new=0, autoraise=True)  # Los enviamos a una calculadora de derivadas

def int():
    url = 'https://es.symbolab.com/solver/integral-calculator/'
    webbrowser.open(url, new=0, autoraise=True) # Los enviamos a una calculadora de integrales

def lim():
    url = 'https://es.symbolab.com/solver/limit-calculator'
    webbrowser.open(url, new=0, autoraise=True) # Los enviamos a una calculadora de límites

def ecu():
    url = 'https://es.symbolab.com/solver/equation-calculator'
    webbrowser.open(url, new=0, autoraise=True) # Los enviamos a una calculadora de ecuaciones

def cal():
    url = 'https://web2.0calc.es/'
    webbrowser.open(url, new=0, autoraise=True)  # Los enviamos a otra calculadora

def mod():
    op1 = float(e_textoal1.get())
    op2 = float(e_textoal2.get())
    op3 = op1 % op2  # Tomamos el resto de la división
    e_texto.delete(0, END)
    e_texto.insert(0, op3)

# Creamos los botones y los añadimos a la ventana
boton1 = Button(ventana, text="1", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(1))
boton2 = Button(ventana, text="2", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(2))
boton3 = Button(ventana, text="3", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(3))
boton4 = Button(ventana, text="4", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(4))
boton5 = Button(ventana, text="5", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(5))
boton6 = Button(ventana, text="6", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(6))
boton7 = Button(ventana, text="7", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(7))
boton8 = Button(ventana, text="8", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(8))
boton9 = Button(ventana, text="9", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(9))
boton0 = Button(ventana, text="0", width = 16, height = 2, background = "#00FFFF", command = lambda: click_boton(0))

boton_borrar = Button(ventana, text="AC", width = 5, height = 2, background = "#00FFFF", command = lambda: borrar())
boton_parentesis1 = Button(ventana, text="(", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=")", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton("."))

boton_div = Button(ventana, text=":", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton("/"))
boton_mult = Button(ventana, text="x", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton("*"))
boton_sum = Button(ventana, text="+", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton("+"))
boton_rest = Button(ventana, text="-", width = 5, height = 2, background = "#00FFFF", command = lambda: click_boton("-"))
boton_igual = Button(ventana, text="=", width = 5, height = 2, background = "#00FFFF", command = lambda: hacer_operacion())

boton_aleatorio = Button(ventana, text="Rand", width = 5, height = 5, background = "#00FFFF", command = lambda: al())
boton_factorial = Button(ventana, text="x!\nOnly int", width = 5, height = 5, background = "#00FFFF", command = lambda: factorial())
boton_log = Button(ventana, text="log", width = 5, height = 5, background = "#00FFFF", command = lambda: logaritmo())
boton_pot = Button(ventana, text="x^y", width = 5, height = 5, background = "#00FFFF", command = lambda: potencia())
boton_raiz = Button(ventana, text="√", width = 5, height = 5, background = "#00FFFF", command = lambda: raiz())
boton_radianes = Button(ventana, text="rad", width = 5, height = 3, background = "#00FFFF", command = lambda: rad())
boton_grados = Button(ventana, text="º", width = 5, height = 3, background = "#00FFFF", command = lambda: grados())
boton_conste = Button(ventana, text="e", width = 5, height = 3, background = "#00FFFF", command = lambda: click_boton(math.e))
boton_constpi = Button(ventana, text="π", width = 5, height = 3, background = "#00FFFF", command = lambda: click_boton(math.pi))
boton_porcentaje = Button(ventana, text="%", width = 5, height = 3, background = "#00FFFF", command = lambda: porcentaje())

boton_seno = Button(ventana, text="sen(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: seno())
boton_coseno = Button(ventana, text="cos(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: coseno())
boton_tangente = Button(ventana, text="tan(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: tangente())
boton_cotangente = Button(ventana, text="cotan(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: cotangente())
boton_secante = Button(ventana, text="sec(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: secante())
boton_cosecante = Button(ventana, text="cosec(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: cosecante())
boton_senh = Button(ventana, text="senh(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: senh())
boton_cosh = Button(ventana, text="cosh(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: cosh())
boton_tanh = Button(ventana, text="tanh(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: tanh())
boton_sech = Button(ventana, text="sech(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: secanteh())
boton_cosech = Button(ventana, text="cosech(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: cosecanteh())
boton_cotanh = Button(ventana, text="cotanh(x)", width = 7, height = 3, background = "#00FFFF", command = lambda: cotangenteh())

boton_ln = Button(ventana, text="ln(x)", width = 21, height = 3, background = "#00FFFF", command = lambda: ln())
boton_exp = Button(ventana, text="e^x", width = 21, height = 3, background = "#00FFFF", command = lambda: ex())
boton_percent = Button(ventana, text="% de", width = 7, height = 3, background = "#00FFFF", command = lambda: percent())
boton_der = Button(ventana, text="derivates solver", width = 14, height = 3, background = "#00FFFF", command = lambda: der())
boton_int = Button(ventana, text="Integral solver", width = 14, height = 3, background = "#00FFFF", command = lambda: int())
boton_lim = Button(ventana, text="Limits solver", width = 14, height = 3, background = "#00FFFF", command = lambda: lim())
boton_ecu = Button(ventana, text="Equations \nsolver", width = 7, height = 17, background = "#00FFFF", command = lambda: ecu())
boton_cal = Button(ventana, text="Other calculators", width = 14, height = 3, background = "#00FFFF", command = lambda: cal())
boton_mod = Button(ventana, text="mod", width = 5, height = 3, background = "#00FFFF", command = lambda: mod())

# Agregar botones a la pantalla
boton_borrar.grid(row = 2, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 2, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 2, column = 3, padx = 5, pady = 5)

boton7.grid(row = 3, column = 0, padx = 5, pady = 5)
boton8.grid(row = 3, column = 1, padx = 5, pady = 5)
boton9.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 3, column = 3, padx = 5, pady = 5)

boton4.grid(row = 4, column = 0, padx = 5, pady = 5)
boton5.grid(row = 4, column = 1, padx = 5, pady = 5)
boton6.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 4, column = 3, padx = 5, pady = 5)

boton1.grid(row = 5, column = 0, padx = 5, pady = 5)
boton2.grid(row = 5, column = 1, padx = 5, pady = 5)
boton3.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_rest.grid(row = 5, column = 3, padx = 5, pady = 5)

boton0.grid(row = 6, column = 0,columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 6, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 6, column = 3, padx = 5, pady = 5)

boton_aleatorio.grid(row = 2, column = 4,columnspan = 1,rowspan = 2, padx = 5, pady = 5)
boton_factorial.grid(row = 4, column = 4,columnspan = 1,rowspan = 2, padx = 5, pady = 5)
boton_raiz.grid(row = 6, column = 4, rowspan = 1, padx = 5, pady = 5)

boton_log.grid(row = 0, column = 10, padx = 5, pady = 5)
boton_pot.grid(row = 1, column = 10, padx = 5, pady = 5)

boton_radianes.grid(row = 2, column = 5, rowspan = 1, padx = 5, pady = 5)
boton_grados.grid(row = 2, column = 6, rowspan = 1, padx = 5, pady = 5)

boton_conste.grid(row = 2, column = 7, rowspan = 1, padx = 5, pady = 5)
boton_constpi.grid(row = 2, column = 8, rowspan = 1, padx = 5, pady = 5)

boton_porcentaje.grid(row = 2, column = 9, rowspan = 1, padx = 5, pady = 5)
boton_mod.grid(row = 2, column = 10, rowspan = 1, padx = 5, pady = 5)

boton_seno.grid(row = 3, column = 6, rowspan = 1, padx = 5, pady = 5)
boton_coseno.grid(row = 3, column = 7, rowspan = 1, padx = 5, pady = 5)
boton_tangente.grid(row = 3, column = 8, rowspan = 1, padx = 5, pady = 5)
boton_cotangente.grid(row = 4, column = 6, rowspan = 1, padx = 5, pady = 5)
boton_secante.grid(row = 4, column = 7, rowspan = 1, padx = 5, pady = 5)
boton_cosecante.grid(row = 4, column = 8, rowspan = 1, padx = 5, pady = 5)
boton_senh.grid(row = 5, column = 6, rowspan = 1, padx = 5, pady = 5)
boton_cosh.grid(row = 5, column = 7, rowspan = 1, padx = 5, pady = 5)
boton_tanh.grid(row = 5, column = 8, rowspan = 1, padx = 5, pady = 5)
boton_sech.grid(row = 6, column = 6, rowspan = 1, padx = 5, pady = 5)
boton_cosech.grid(row = 6, column = 7, rowspan = 1, padx = 5, pady = 5)
boton_cotanh.grid(row = 6, column = 8, rowspan = 1, padx = 5, pady = 5)

boton_ln.grid(row = 8, column = 0, rowspan = 1, columnspan = 3, padx = 5, pady = 5)
boton_exp.grid(row = 8, column = 3, rowspan = 1, columnspan = 3, padx = 5, pady = 5)
boton_percent.grid(row = 8, column = 8, rowspan = 1, columnspan = 1, padx = 5, pady = 5)
boton_der.grid(row = 3, column = 9, rowspan = 1, columnspan = 2, padx = 5, pady = 5)
boton_int.grid(row = 4, column = 9, rowspan = 1, columnspan = 2, padx = 5, pady = 5)
boton_lim.grid(row = 5, column = 9, rowspan = 1, columnspan = 2, padx = 5, pady = 5)
boton_cal.grid(row = 6, column = 9, rowspan = 1, columnspan = 2, padx = 5, pady = 5)
boton_ecu.grid(row = 3, column = 5, rowspan = 4, columnspan = 1, padx = 5, pady = 5)
ventana.mainloop()  # Mostramos la ventana