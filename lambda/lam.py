#la funcion lambda sirve para crear funciones simples

area_triangulo=lambda base, altura:(base*altura)/2 # los 2 puntos es lo mismo que un return

print (area_triangulo(7,5))

t1=area_triangulo(3,5)
t2=area_triangulo(7,4)
t3=area_triangulo(18,23)

print ("Area triangulo 1 es= ",t1," Area triangulo 2 es= ",t2," Area triangulo 3 es= ",t3)

destacar_valor=lambda comision:"!{} €!".format(comision)
comision_john= 123454
print (destacar_valor(comision_john))