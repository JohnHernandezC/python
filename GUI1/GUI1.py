from tkinter import *

raiz=Tk()
raiz.title("Primera GUI")
raiz.resizable(1,1)# uno y cero es lo mismo que true y false
raiz.iconbitmap("icono.ico") # se puede modificar la ruta
#raiz.geometry("650x350")#tamaño ventana
raiz.config(bg="blue")
raiz.config(bd=40)
raiz.config(relief="sunken")#otro borde sunken

miframe=Frame(raiz, width="650", height="350" )

miframe.pack(fill="both", expand="true")#side="left", anchor="n"
miframe.config(bg="red")
miframe.config(width="650", height="350")
miframe.config(bd=35)
miframe.config(relief="groove")#otro borde sunken
miframe.config(cursor="pirate")# otro cursor hand2
miframe=Frame(raiz, width="650", height="350" )
milabel = Label(miframe, text="hola mi nombre es")
milabel.place(x=100, y=200)



raiz.mainloop()

