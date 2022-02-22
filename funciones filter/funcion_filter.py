#---------------------------------------------------------------------------
#VERIFICA QUE LOS ELEMENTOS DE UNA SECUENCIOA CUMPLAN UNA CONDICION DEVOLVIENDO UN ITERADOR CON LOS ELEMETOS QUE LA CUMPLAN
#--------------------------------------------------------------------------
def numeroPar(num):
    if num %2==0:# significa: si el numero es divisible por 2
        return True

numeros=[17,32,43,65,56,76,45,12,98,34,65,]

print(list(filter(numeroPar,numeros)))

print(list(filter(lambda numerosPares:numerosPares%2==0,numeros)))


class empleados():
    def __init__(self,nombre,cargo,salario):#constructor
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)
empleado=[
empleados("ana","gerente",3234554),
empleados("pedro","secretaria",3234),
empleados("maria","ingeniero",554),
empleados("jose","medico",4554),
]

salarios_altos=filter(lambda empleado:empleado.salario>4000, empleado)

for i in salarios_altos:
    print(i)