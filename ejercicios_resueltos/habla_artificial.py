import pyttsx3
from tkinter import *

class MainWindow:
    def __init__(self):
        self.engine = pyttsx3.init()  # Inicializamos el motor de texto a voz
        self.engine.setProperty('rate', 120)
        self.window = Tk()  # Creamos la ventana
        self.window.title("Habla Artificial")
        self.window.configure(background='white')

        # Creamos los Widgets y los añadimos a la ventana
        self.entry = Entry(self.window, width=50, font="Arial 20")
        self.entry.grid(row=0, column=0)
        self.button = Button(self.window, font="Arial 20", text="Hablar", command=lambda: self.hablar(self.entry.get()))
        self.button.grid(row=1, column=0)

    def hablar(self, texto):  # Creamos la función para hablar
        self.engine.say(texto)
        self.engine.runAndWait()


if __name__ == '__main__':
    win = MainWindow()     # Instanciamos la clase principal
    win.window.mainloop()  # Mostramos la ventana