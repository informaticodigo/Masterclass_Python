from tkinter import *
from tkinter.messagebox import showerror
import matplotlib.pyplot as plt
from math import *
import numpy as np

# Para mostrar varias opciones, esta vez trabajaremos la ventana 
# desde una clase

class Graficadora():

    def __init__(self):
        # Creamos la ventana y la configuramos
        self.window = Tk()
        self.window.title('Graficadora')
        self.window.resizable(False, False)
        
        # Creamos los widgets y los añadimos a la ventana
        self.entry = Entry(self.window, font="Arial 14", width=61)
        self.entry.grid(row=0, column=0, columnspan=2)
        self.entry.focus()
        
        self.range1 = Entry(self.window, font="Arial 14", width=30)
        self.range1.grid(row=1, column=0, columnspan=1)
        self.range1.focus()
        
        self.range2 = Entry(self.window, font="Arial 14", width=30)
        self.range2.grid(row=1, column=1, columnspan=1)
        self.range2.focus()

        self.button = Button(self.window, font="Arial 14", width=61, text='Graficar', command=lambda: self.graficar(self.entry.get(), int(self.range1.get()), int(self.range2.get())))
        self.button.grid(row=2, column=0, columnspan=2)
    
    def graficar(self, funcion, xmin=-10, xmax=10):
        try:
            # Creamos una matriz de numpy entre xmin y xmax con una resolución de 0.1
            x = np.linspace(xmin,xmax,xmax-xmin*10)

            # evaluamos la función para todo x
            y = eval(funcion)

            # Personalizamos el gráfico
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')

            # creamos la gráfica
            plt.plot(x,y, 'r')

            # enseñamos la gráfica
            plt.show()
        except:
            try:
                # Creamos una matriz de numpy entre xmin y xmax con una resolución de 0.1
                x = np.linspace(xmin,xmax,xmax-xmin*10)

                # Añadimos x*0 por si el error es que el usuario ha introducido una constante sin x
                y = eval(funcion+"+x*0")

                # Personalizamos el gráfico
                fig = plt.figure()
                ax = fig.add_subplot(1, 1, 1)
                ax.spines['left'].set_position('center')
                ax.spines['bottom'].set_position('zero')
                ax.spines['right'].set_color('none')
                ax.spines['top'].set_color('none')
                ax.xaxis.set_ticks_position('bottom')
                ax.yaxis.set_ticks_position('left')

                # Creamos la gráfica
                plt.plot(x,y, 'r')

                # Enseñamos la gráfica
                plt.show()
            except:
                showerror('Error', 'La función debe estar escrita con "x" y las multiplicaciones con *')  # mostramos un mensaje de error


if __name__ == '__main__':
    graficadora = Graficadora()    # Instanciamos nuestra clase principal
    graficadora.window.mainloop()  # Mostramos la ventana