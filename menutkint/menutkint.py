from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog

# Configuración de la raíz
root = Tk()



menubar = Menu(root)
root.config(menu=menubar)

def test(): #importar una ventana emergente
    color = ColorChooser.askcolor(title="Elige un color")
    print(color)
def cerrar():
  resultado = MessageBox.askquestion("Salir", "¿Está seguro que desea salir sin guardar?")

  if resultado == "yes":
    root.destroy() 


def test2():
    #se puede elegir el tipo de archivo
    fichero = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="Imágenes")#filetypes=(("Imagenes","*.jpg"),("fichetos de textos","*.txt"))
    print(fichero)#aqui se almacena la direccion del archivo

filemenu = Menu(menubar, tearoff=0)#tearoff hace que quite la lagrima
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir" , command=test2)
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar", command=test)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
filemenu.add_command(label="Salir 2", command=cerrar)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Finalmente bucle de la aplicación
root.mainloop()
