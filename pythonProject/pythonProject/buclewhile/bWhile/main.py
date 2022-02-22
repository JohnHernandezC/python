import math
i=1
while i<=10:
     print("ejecucion: "+str(i))
     i=i+1

print("bucle finalizado")

edad=int(input("intoduce la edad"))
while edad<5 or edad>100:
     print("haz intoducido una edad incorrecta intentalo de nuevo")
     edad = int(input("intoduce la edad de nuevo"))

print("gracias... ")
print("la edad es: "+str(edad))


print("programa que calcule la raiz caudrada de un numero")
numero=int(input("ingrese un numero"))

intentos=0
while numero<0:
     print("no se puede obtener la raiz de un numero negativo")
     if intentos==2:
         print("te haz quedado sin intentos")
         break;

     numero = int(input("ingrese un numero"))
     if numero<0:
         intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("la raiz caudrada de: "+str(numero)+" es "+str(solucion))

for i in "python":

    if i=="h":
        continue #salta el bucle en el que se imprime la h

    print("viendo la letra "+ i )

nombre="john hernadez"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)
