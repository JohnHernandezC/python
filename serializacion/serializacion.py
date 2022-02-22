import pickle

#crear y guardar los archivos codificados
#lista_nombres=["Pedro","Ana","Maria","Juan"]
#fichero_binario=open("lista_nombres","wb")
#pickle.dump(lista_nombres, fichero_binario)
#fichero_binario.close()

#ver losarchivos codificados
#fichero=open("lista_nombres" ,"rb")
#lista=pickle.load(fichero)
#print(lista)

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

coche1=vehiculos("mazda","345")
coche2=vehiculos("audi","792")
coche3=vehiculos("ferrary","343")
coches=[coche1,coche2,coche3]
fichero=open("coche", "wb")
pickle.dump(coches, fichero)
fichero.close()
del (fichero)

fichero_apertura=open("coche" ,"rb")
lista=pickle.load(fichero_apertura)
fichero_apertura.close()
for p in lista:
 print(p.estado())

