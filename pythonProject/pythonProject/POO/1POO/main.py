#CLASE es donde se almacena el conjunto de atributos
# que son generales en todo el programa
#METODO Comportamientos que tiene el objeto
#MODULARISACION se puede dividir en distintas areas por si alguna falla las demas siguen respondiendo
#ENCAPSULAMIENTO proteger lso archivos del esxterior


class Coche():  #class para crear clase
    def __init__(self):# Metodo constructor
       self.__largo_chasis=250
       self.__ancho_chasis=120
       self.__ruedas=4 #los 2 guiones son para encapsular y que nadie la modifique
       self.__enmarcha=False

  #defs pertenece a la clase def no pertenece a la clase

    def arrancar(self,arrancamos): #metodo

        self.enmarcha=arrancamos

        if (self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"

    def estado(self):
        print("el auto tiene " ,self.__ruedas ," Ruedas y un ancho de"  ,self.__ancho_chasis  ," y un lardo de "  ,self.__largo_chasis)


miCoche = Coche() #esto es una instancia o crear un objeto


print(miCoche.arrancar(True))
miCoche.estado()

print("aqui se crea un segundo objeto")

miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()
