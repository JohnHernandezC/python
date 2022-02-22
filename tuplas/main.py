#las tuplas son listas inmutables

mi_tupla=("juan","maria",1,2,3,4,5,4,6,3,1,2)
mi_lista=list(mi_tupla)#convertir tupla en lista para hacer lo contrario tuple(mi_lista)
print(mi_tupla[:])
print(mi_lista[:])
print("juan" in mi_tupla) #buscar
print(mi_tupla.count(3))#contar cuantas veces se encuentra un elemnto
print(len(mi_tupla))#cuantos elementos hay en la mi_tupla

mi_tupla1=("juan",13,1,1995)
nombre,dia,mes,agno=mi_tupla1
print(nombre)
print(dia)
print(mes)
print(agno)

