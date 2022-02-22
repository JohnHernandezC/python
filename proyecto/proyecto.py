from tkinter import *
from tkinter import messagebox as MessageBox
import sqlite3

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

def resetCampos():
    miId.set("")
    miName.set("")
    miApellido.set("")
    miDirec.set("")
    miPass.set("")
    textoLargo.delete(1.0, END)

def insertar():
    miConexion=sqlite3.connect("baseF")
    miCursor=miConexion.cursor()
#INSERTAR UN DATO
    """"miCursor.execute("INSERT INTO productos_dos VALUES(NULL, '"+ miName.get() +
                                                      "','"+ miApellido.get() +
                                                      "','"+ miDirec.get() +
                                                      "','"+ miPass.get() +
                                                      "','"+ textoLargo.get("1.0", END)+ "')")"""
#consulta parametrisada
    datosPa=miName.get(),miApellido.get(),miDirec.get(),miPass.get(),textoLargo.get("1.0",END)
    miCursor.execute("INSERT INTO productos_dos VALUES(NULL,?,?,?,?,?)",(datosPa))


    miConexion.commit()
    MessageBox.showinfo("BBDD", "se a insertado con exito el registro")
def mostrarBBDD():
    miConexion=sqlite3.connect("baseF")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM productos_dos WHERE ID=" + miId.get())
    varios=miCursor.fetchall()# esto trae todos los datos en forma de lista
    for i in varios:
        miId.set(i[0])
        miName.set(i[1])
        miApellido.set(i[2])
        miDirec.set(i[3])
        miPass.set(i[4])
        textoLargo.insert(1.0,i [5])
    miConexion.commit()


def modificar():
    miConexion=sqlite3.connect("baseF")
    miCursor=miConexion.cursor()

    """miCursor.execute("UPDATE productos_dos SET nombre='"+ miName.get() + 
                                              "', apellido='"+ miApellido.get()+
                                              "', direccion='"+ miDirec.get()+
                                              "', contraseña='"+ miPass.get()+
                                              "', comentarios='"+ textoLargo.get("1.0", END)+
                                              "' WHERE ID="+ miId.get())"""

    #consulta parametrisada
    datosPa=miName.get(),miApellido.get(),miDirec.get(),miPass.get(),textoLargo.get("1.0",END)
    miCursor.execute("UPDATE productos_dos SET nombre=?,apellido=?,direccion=?,contraseña=?,comentarios=?"+ 
                                                                            "WHERE ID="+ miId.get(),(datosPa))
    miConexion.commit()
    MessageBox.showinfo("BBDD", "se a actualizado con exito el registro")

#------------------------------------------------------------------------------


# Configuración de la raíz
root = Tk()
miframe=Frame(root )
miframe.pack()


menubar = Menu(root)
root.config(menu=menubar)


def cerrar():
  resultado = MessageBox.askquestion("Salir", "¿Está seguro que desea salir sin guardar?")

  if resultado == "yes":
    root.destroy() 




filemenu = Menu(menubar, tearoff=0)#tearoff hace que quite la lagrima
filemenu.add_command(label="Nuevo", command=crear)
filemenu.add_command(label="Abrir" )
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)



editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Limpiar campos", command=resetCampos)
editmenu.add_command(label="insertar", command=insertar)
editmenu.add_command(label="buscar", command=mostrarBBDD)
editmenu.add_command(label="modificar", command=modificar)
editmenu.add_command(label="Eliminar",command=delete)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

miframe=Frame(root, width="1200", height="600" )
miframe.pack()
 
miId=StringVar()#esto nos ayuda a decirle al programa que los datos en los campos entry son string
miName=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDirec=StringVar()


idB=Entry(miframe, textvariable=miId ) #luego de convertir los entry a estring se definen aqui
idB.grid(row=0, column=1)
idB.config(fg="red")
cuadro=Entry(miframe, textvariable=miName) 
cuadro.grid(row=1, column=1)
cuadro.config(fg="red")
cuadro1=Entry(miframe,textvariable=miApellido)
cuadro1.grid(row=2, column=1)
cuadro1.config(fg="yellow")# se puede configurar las caracterizticas desde config
cuadro2=Entry(miframe, textvariable=miDirec)
cuadro2.grid(row=3, column=1)
cuadro2.config(fg="blue")
cuadro3=Entry(miframe,textvariable=miPass)
cuadro3.grid(row=4, column=1)
cuadro3.config(fg="red", justify="right", show="*")
textoLargo=Text(miframe, width=16, height=5)#crear un caudro de texto
textoLargo.grid(row=5, column=1)
scroolver=Scrollbar(miframe, command=textoLargo.yview)#configuramos el scroll 
scroolver.grid(row=5, column=2,sticky="nsew",)
textoLargo.config(fg="red", yscrollcommand=scroolver.set)#pacicionamiento del scroll


milabel = Label(miframe, text="ID", fg="black", font=("New Roman", 12))
milabel.grid(row=0, column=0, sticky="w", padx=15, pady=15) 
milabel = Label(miframe, text="Nombre", fg="black", font=("New Roman", 12))
milabel.grid(row=1, column=0, sticky="w", padx=15, pady=15) 
milabel1 = Label(miframe, text="apellido", fg="black", font=("New Roman", 12))
milabel1.grid(row=2, column=0, sticky="w", padx=15, pady=15 )
milabel2 = Label(miframe, text="direccion", fg="black", font=("New Roman", 12))
milabel2.grid(row=3, column=0, sticky="w", padx=15, pady=15) #, padx=15, pady=15 agrega espacios por pixeles
milabel3 = Label(miframe, text="contraseña", fg="black", font=("New Roman", 12))
milabel3.grid(row=4, column=0, sticky="w", padx=15, pady=15 )
milabel4 = Label(miframe, text="comentarios", fg="black", font=("New Roman", 12))
milabel4.grid(row=5, column=0, sticky="w", padx=15, pady=15 )

miframe2=Frame(root)
miframe2.pack()

insertDatos=Button(miframe2, text="Insertar", width=7 ,command=insertar)
insertDatos.grid(row=7, column=0 )
mostrarDatos=Button(miframe2, text="Mostrar", width=7, command=mostrarBBDD )
mostrarDatos.grid(row=7, column=1)
modificarDatos=Button(miframe2, text="Modificar", width=7, command=modificar)
modificarDatos.grid(row=7, column=2)
eliminarDatos=Button(miframe2, text="Eliminar", width=7, command=delete)
eliminarDatos.grid(row=7, column=3 )

# Finalmente bucle de la aplicación
root.mainloop()

