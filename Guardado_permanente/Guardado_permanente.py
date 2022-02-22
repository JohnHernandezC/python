import pickle
class persona:
    def __init__ (self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("se a creado una nueva persona con el nombre ", self.nombre)

    def __str__(self):
     return "{} {} {}".format(self.nombre, self.genero, self.edad) #almacena en modo lista

class listaperonas:
     personas=[]
     def __init__(self):
         listaper=open("fichero externo", "ab+")
         listaper.seek(0)
         try:#detecta si la lista esta vacia la primera vez
           self.personas=pickle.load(listaper)#nos da la informacion de las personas que estan almacenadas y se cargaron
           print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
         except:
             print("el fichero esta vacio")
         finally:
             listaper.close()
             del(listaper)

     def agregar(self, p):
         self.personas.append(p)
         self.guardarEnFicheroExterno()
         

     def mostrar(self):
         for p in self.personas:
             print(p)

     def guardarEnFicheroExterno(self):
         listaper=open("fichero externo", "wb")
         pickle.dump(self.personas, listaper)
         listaper.close()
         del(listaper)

     def mostrarinfoFicheroExterno(self):
         print("la informacion del fichero externo es la siguiente")
         for p in self.personas:
             print(p)



miLista=listaperonas()
perso=persona("mario","m","12")
miLista.agregar(perso)#despues de añadir los datos se crea la lista y se envia a agregar
miLista.mostrarinfoFicheroExterno()






