class coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")

class moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")

class camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")



def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()#recibe un objeto por marametro para llamar al metodo desplazamiento

miVehiculo5=camion()
desplazamientoVehiculo(miVehiculo5)
     
