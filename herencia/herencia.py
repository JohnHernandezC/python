class vehiculos():

    def __init__(self, marca, modelo):
     self.marca=marca
     self.modelo=modelo
     self.enmarcha=False
     self.acelera=False
     self.frena=False

    def arrancar(self):
         self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca, "\nModelo:",self.modelo, "\nEnmarcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ",self.frena)
class Furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return" la furgoneta no esta cargada"


class Moto(vehiculos):
    hCaballito=""

    def caballito(self):
        self.hCaballito="estoy haciendo caballito"

    def estado(self):
        print("Marca: ",self.marca, "\nModelo:",self.modelo, "\nEnmarcha: ",
             self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ",self.frena,"\n",self.hCaballito)

class vElectricos(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)

        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True

class biciElectrica(vElectricos,vehiculos):
    
    pass


miMoto=Moto("Honda" , "CBR")
miMoto.caballito()
miMoto.estado()
miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
miBici=biciElectrica("orbea","thj")
miBici.estado()



    

