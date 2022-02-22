from tkinter import *

raiz=Tk()

miframe=Frame(raiz, width="1200", height="600" )
miframe.pack()
reset_pantalla=False
operacion=""
resultado=0
#-------------pantalla-----------------
numeroP=StringVar()
pantalla=Entry(miframe, textvariable=numeroP)#asociamos de nuevo la pantalla
pantalla.grid(row=1, column=1, padx=15, pady=15,columnspan=4)#el column nos ayuda a distribuir la pantalla por los cuatro espacios de botones
pantalla.config(background="black",fg="pink", justify="right")

#-------------botones------------------
#-------------funciones----------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroP.set(num)
        reset_pantalla=False
    else:
        numeroP.set(numeroP.get()+num)

def suma (num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=int(num)
    operacion="suma"
    reset_pantalla=True
    numeroP.set(resultado)

contador_resta=0
def resta (num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla
    resultado-=int(num)
    operacion="resta"
    numeroP.set(resultado)

    if contador_resta==0:
      num1=int(num)
      resultado=num1
    else:

      if contador_resta==1:
       resultado=num1-int(num)
      else:
        resultado=int(resultado)-int(num)	
      numeroP.set(resultado)
      resultado=numeroP.get()
    contador_resta=contador_resta+1
    operacion="resta"
    reset_pantalla=True

contador_multi=0
def multiplicacion (num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla
    resultado*=int(num)
    operacion="multiplicacion"
    numeroP.set(resultado)

    if contador_multi==0:
      num1=int(num)
      resultado=num1
    else:

      if contador_multi==1:
       resultado=num1-int(num)
      else:
        resultado=int(resultado)*int(num)	
      numeroP.set(resultado)
      resultado=numeroP.get()
    contador_multi=contador_multi+1
    operacion="multiplicacion"
    reset_pantalla=True

contador_div=0
def division (num):
    global operacion
    global resultado
    global num1
    global contador_div
    global reset_pantalla
   

    if contador_div==0:
      num1=float(num)
      resultado=num1
    else:

      if contador_div==1:
       resultado=num1/float(num)
      else:
        resultado=float(resultado)/float(num)		
      numeroP.set(resultado)
      resultado=numeroP.get()
    contador_div=contador_div+1
    operacion="division"
    reset_pantalla=True

def Elresultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_div
    if operacion=="suma":
      numeroP.set(resultado+int(numeroP.get()))
      resultado=0
    elif operacion=="resta":
      numeroP.set(int(resultado)-int(numeroP.get()))
      resultado=0
      contador_resta=0
    elif operacion=="multiplicacion":
      numeroP.set(int(resultado)*int(numeroP.get()))
      resultado=0
      contador_multi=0
    elif operacion=="division":
      numeroP.set(int(resultado)/int(numeroP.get()))
      resultado=0
      contador_div=0
      
#-------------fila 1-------------------
boton7=Button(miframe, text="7", width=3, command=lambda:numeroPulsado("7") )
boton7.grid(row=2, column=1 )
boton8=Button(miframe, text="8", width=3, command=lambda:numeroPulsado("8") )
boton8.grid(row=2, column=2)
boton9=Button(miframe, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botondiv=Button(miframe, text="/", width=3, command=lambda:division(numeroP.get()))
botondiv.grid(row=2, column=4 )

#-------------fila 2-------------------
boton4=Button(miframe, text="4", width=3, command=lambda:numeroPulsado("4") )
boton4.grid(row=3, column=1 )
boton5=Button(miframe, text="5", width=3, command=lambda:numeroPulsado("5") )
boton5.grid(row=3, column=2)
boton6=Button(miframe, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonx=Button(miframe, text="x", width=3, command=lambda:multiplicacion(numeroP.get()))
botonx.grid(row=3, column=4 )

#-------------fila 3-------------------
boton1=Button(miframe, text="1", width=3, command=lambda:numeroPulsado("1") )
boton1.grid(row=4, column=1 )
boton2=Button(miframe, text="2", width=3, command=lambda:numeroPulsado("2") )
boton2.grid(row=4, column=2)
boton3=Button(miframe, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonsres=Button(miframe, text="-", width=3, command=lambda:resta(numeroP.get()))
botonsres.grid(row=4, column=4 )

#-------------fila 4-------------------
boton0=Button(miframe, text="0", width=3, command=lambda:numeroPulsado("0") )
boton0.grid(row=5, column=1 )
botoncom=Button(miframe, text=",", width=3, command=lambda:numeroPulsado(",") )
botoncom.grid(row=5, column=2)
botonigual=Button(miframe, text="=", width=3, command=lambda:Elresultado())
botonigual.grid(row=5, column=3)
botonsum=Button(miframe, text="+", width=3, command=lambda:suma(numeroP.get()))
botonsum.grid(row=5, column=4 )

raiz.mainloop()
