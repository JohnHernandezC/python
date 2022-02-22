def divide():
 try:
    op1=(float(input("introduce el primer numero")))
    op2 = (float(input("introduce el segundo numero")))
    print("la deivicion es" +str(op1/op2))
 except ValueError:

     print("el valor introducido es incorrecto")


 except ZeroDivisionError:
    print("no se puede dividir entre cero")

    print("calculo fializado")

divide()


def evaluar_edad(edad):
    if edad<0:
        raise TypeError("nadie es menor de 0")
    if edad<20:
        return "Eres muy joven"
    elif  edad<40:
        return "eres joven"
    elif  edad<65:
        return "eres maduro"
    elif  edad<100:
        return "cuidate!!!"
print(evaluar_edad(-1))





