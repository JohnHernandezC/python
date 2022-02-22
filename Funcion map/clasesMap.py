class empleados():
    def __init__(self,nombre,cargo,salario):#constructor
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)
empleado=[
empleados("ana","gerente",6700),
empleados("pedro","secretaria",3234),
empleados("maria","ingeniero",5543),
empleados("jose","medico",4554),
]

def calculoAumento(empleado):
    if (empleado.salario<4600):
     empleado.salario=empleado.salario*1.03
    return empleado
listaEmpleados=map(calculoAumento,empleado)

for i in listaEmpleados:
    print(i)