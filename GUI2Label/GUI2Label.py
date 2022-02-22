from tkinter import *

raiz=Tk()

miframe=Frame(raiz, width="1200", height="600" )
miframe.pack()

minombre=StringVar()


#imagen=PhotoImage(file="as.gif")
##milabel2 = Label(miframe, image=imagen)
#milabel2.place(x=0, y=0)

#cuadro de texto
cuadro=Entry(miframe, textvariable=minombre) #texvariable nos ayuda a asociar conlos diferentes variales un cuadro
cuadro.grid(row=0, column=1)
cuadro.config(fg="red")
cuadro1=Entry(miframe)
cuadro1.grid(row=1, column=1)
cuadro1.config(fg="yellow")# se puede configurar las caracterizticas desde config
cuadro2=Entry(miframe)
cuadro2.grid(row=2, column=1)
cuadro2.config(fg="blue")
cuadro3=Entry(miframe)
cuadro3.grid(row=3, column=1)
cuadro3.config(fg="red", justify="right", show="*")
textoLargo=Text(miframe, width=16, height=5)#crear un caudro de texto
textoLargo.grid(row=4, column=1)
scroolver=Scrollbar(miframe, command=textoLargo.yview)#configuramos el scroll 
scroolver.grid(row=4, column=2,sticky="nsew",)
textoLargo.config(fg="red", yscrollcommand=scroolver.set)#pacicionamiento del scroll


milabel = Label(miframe, text="nombre", fg="red", font=("Comic Sans MS", 18))
milabel.grid(row=0, column=0, sticky="w", padx=15, pady=15) 
milabel1 = Label(miframe, text="apellido", fg="red", font=("Comic Sans MS", 18))
milabel1.grid(row=1, column=0, sticky="w", padx=15, pady=15 )
milabel2 = Label(miframe, text="direccion", fg="red", font=("Comic Sans MS", 18))
milabel2.grid(row=2, column=0, sticky="w", padx=15, pady=15) #, padx=15, pady=15 agrega espacios por pixeles
milabel3 = Label(miframe, text="contraseña", fg="red", font=("Comic Sans MS", 18))
milabel3.grid(row=3, column=0, sticky="w", padx=15, pady=15 )
milabel4 = Label(miframe, text="comentarios", fg="red", font=("Comic Sans MS", 18))
milabel4.grid(row=4, column=0, sticky="w", padx=15, pady=15 )

#crear y configurar un boton
def codigoBoton ():
    minombre.set("john hernandez")

botonEnvio=Button(miframe, text="Enviar", command=codigoBoton)
botonEnvio.grid(row=5, column=1, padx=15, pady=15 )

raiz.mainloop()