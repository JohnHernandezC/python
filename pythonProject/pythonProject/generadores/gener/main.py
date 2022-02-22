def genera_Pares(limite):#funcion noraml para obtener numeros pares

    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num+=1

    return milista

print(genera_Pares(10))


def genera_Pares2(limite):#funcion con generador

    num=1

    while num<limite:
      yield num*2
      num+=1
devuelve=genera_Pares2(10)

#for i in devuelve:
    #print(i)

print(next(devuelve))

print("mas codigo")
print(next(devuelve))

print("mas codigo")
print(next(devuelve))

print("mas codigo")

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devuelve_ciudades("bogota","medellin","barranquilla",)
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))




