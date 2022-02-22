def funcionDecoradora(funcionparametro):
    def funcionInterior():
        print("vamos a hacer una operacion")
        funcionparametro()
        print("terminamos el calculo")
    return funcionInterior


@funcionDecoradora
def suma():
    print(15+20)

def resta():
    print(55-20)

suma()
resta()