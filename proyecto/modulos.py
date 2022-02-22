import sqlite3
from tkinter import *

from tkinter import messagebox as MessageBox

#funciones
def crear():
   try:
    miConexion=sqlite3.connect("baseF")
    miCursor=miConexion.cursor()
    miCursor.execute('''CREATE TABLE productos_dos (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(50), 
                    apellido VARCHAR(50), 
                    direccion VARCHAR(50), 
                    contraseña VARCHAR(50), 
                    comentarios VARCHAR(100))''')
    MessageBox.showinfo("BBDD", "La base de datos se a creado correctamente")
   except:
       MessageBox.showwarning("ATENCION", "La base de datos ya existe")

def delete():
    miConexion=sqlite3.connect("baseF")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM productos_dos WHERE ID="+ miId.get())
    miConexion.commit()
    MessageBox.showinfo("BBDD", "se a eliminado con exito el registro")

 
#------------------------------------------------------------------------------
miId=StringVar()#esto nos ayuda a decirle al programa que los datos en los campos entry son string
miName=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDirec=StringVar()
