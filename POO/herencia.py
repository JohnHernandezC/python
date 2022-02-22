class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar (self):
        self.enmarcha=True
    def acelerar (self):
        self.acelera=True
    def frena (self):
        self.frena=False
    def estado (self):
        print("Marca: ",self.marca,"\n Modelo: ",self.modelo,"\n En marcha: ",self.enmarcha,"\n Acelerando: ",self.acelera,"\n Frenando: ",self.frena)
class furgoneta(vehiculos):

    def carga (self, cargar):
        self.cargado=cargar

        if(self.cargado):
         return "la furgoneta esta cargada"
        else:
         return "la furgoneta no essta cargada"

class vElectricos(vehiculos):
    def __init__(self,marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargandoEnergia=True

    


class moto(vehiculos):
    caballito=""
    def caballitos(self):
        self.caballito="estoy haciendo un caballito"
    def estado (self):
        print("Marca: ",self.marca,"\n Modelo: ",self.modelo,"\n En marcha: ",self.enmarcha,"\n Acelerando: ",self.acelera,"\n Frenando: ",self.frena,"\n Caballito: ",self.caballito)
    

class bicicletaE(vElectricos, vehiculos):
    pass

mimoto=moto("chevrolet","2012")
miFurgneta=furgoneta("audi","2011")
mimoto.caballitos()
mimoto.estado()

miFurgneta.arrancar()
miFurgneta.estado()
print(miFurgneta.carga(True))

bici=bicicletaE("orbea","Hcrt")