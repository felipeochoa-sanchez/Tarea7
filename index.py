from tkinter import ttk
from tkinter import *

import sqlite3

class biblioteca:

    def __init__(self, ventana):
        self.wind = ventana
        self.wind.title('Programacion Avanzada II, Proyecto Final')
        

        Notebook = ttk.Notebook(ventana)
        Notebook.grid()

        pest =ttk.Frame(Notebook)
        pest1 =ttk.Frame(Notebook)
        pest2 =ttk.Frame(Notebook)
        Notebook.add(pest, text='Ingresar Libros')
        Notebook.add(pest1, text='Stock de Libros')
        Notebook.add(pest2, text='Reservar')

        Label(pest, text = 'Registro de Libros').grid(row = 4, column = 1, columnspan = 1, pady = 1)

        Label(pest, text = 'Nombre del libro: ').grid(row = 6, column = 0)
        self.nombre = Entry(pest)
        self.nombre.focus()
        self.nombre.grid(row = 6, column = 1)

        Label(pest, text = 'Autor: ').grid(row = 8, column = 0)
        self.autor = Entry(pest)
        self.autor.focus()
        self.autor.grid(row = 8, column = 1)

        Label(pest, text = 'Descripción: ').grid(row = 10, column = 0)
        self.desc = Entry(pest)
        self.desc.focus()
        self.desc.grid(row = 10, column = 1)

        Label(pest, text = 'Año de publicación ').grid(row = 12, column = 0)
        self.anio = Entry(pest)
        self.anio.focus()
        self.anio.grid(row = 12, column = 1)

        Label(pest, text = 'Stock disponible ').grid(row = 14, column = 0)
        self.stock = Entry(pest)
        self.stock.focus()
        self.stock.grid(row = 14, column = 1)

        Label(pest, text = 'Tipo de prestamo ').grid(row = 16, column = 0)
        self.tipo = Entry(pest)
        self.tipo.focus()
        self.tipo.grid(row = 16, column = 1)

        # Button Add Product / command = self.add_product)
        ttk.Button(pest, text = 'Guardar Libro').grid(row = 18, columnspan = 2, sticky = W + E)


          # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 4)
        self.tree.heading('#0', text = 'Nombre del Libro', anchor = CENTER)
        self.tree.heading('#1', text = 'Autor', anchor = CENTER)
        

if __name__ =='__main__':
    ventana =Tk()
    application = biblioteca(ventana)
    ventana.mainloop()