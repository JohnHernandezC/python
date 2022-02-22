print("programa de evaluacion de alumnos")
nota_alumno=input("introduce la nota: ")
def evaluacion(nota):
    valoracion="aprovado"
    if nota<5:
        valoracion="suspendido"
    return valoracion
print(evaluacion(int(nota_alumno)))


print("verificacion de acceso")
edad_verificacion=int(input("introduce tu edad"))

if edad_verificacion<18:
     print("no puede pasar")

elif edad_verificacion>100:
    print("esta muy viejo para ingresar")

else:
      print("puedes pasar")

print("el programa a finalizado")

#########SWICH

edad=7

if 0<edad<100: #se pueden crear con varios operadores
    print("edad correcta")
else:
    print("edad incorrecta")

salario_presidente=int(input("ingrese el salario del presidente"))
print("salario presidente "+str(salario_presidente))

salario_director=int(input("ingrese el salario del presidente"))
print("salario director "+str(salario_director))

salario_jefe_area=int(input("ingrese el salario del presidente"))
print("salario jefe de area "+str(salario_jefe_area))

salario_administrativo=int(input("ingrese el salario del presidente"))
print("salario administrativo "+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("todo funciona correctamenta")
else:
    print("algo falla")

#uso and or (if 5<2 and 2>8)

print("asignaturas optativas")
print("informatica grafica-pruebas de sotware-usabilidad y accesibilidad")
datoo=input("escribir la asignatura elegida")
asignatura=datoo.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("asignatura elgida"+asignatura)
else:
    print("la asignatura elegida no esta disponible")#lower() upper() convierte a minuscula y mayuscula


