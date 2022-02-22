class Coche():
    def __init__(self):
        self.largoCh=250
        self.anchoCh=120
        self.__ruedasCo=4 #para encapsular una variable se debe agregar 2 guiones
        self.__enMarcha=False
    
    

    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos

        if(self.__enMarcha):
            chequeo=self.__chequeo_interno()
       
        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enMarcha and chequeo==False):
            print("algo a ido mal en el chequeo")
        else:
            return "el coche no esta en marcha"


    def estado(self):
        print("el coche tiene", self.__ruedasCo, " ruedas  un ancho de ", self.anchoCh, " metros y un largo de", self.largoCh, " metros.")

    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.aceite=="ok" and self.gasolina=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

     
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()
print("-----------------------------")

miCoche2=Coche()
miCoche._Coche__ruedasCo=7
miCoche2.largoCh=200
print(miCoche2.arrancar(False))
miCoche2.estado()