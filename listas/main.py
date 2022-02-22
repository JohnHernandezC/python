mi_listas = [1, 2, 3, 4, "john", 1.234, True]  #se puede usar varios tiposde datos

mi_listas2 = ["maria", "juanita", "latina", "morenita"] #colocano*3 la lista se repetira 3 veces

mi_listas2.append("sofai")  #añade otro dato a la lista
mi_listas2.append("karla")  #añade otro dato a la lista

mi_listas2.insert(2, "luisa")  #añade a un lugar espesifico de la lista

mi_listas.extend([4, 3, 2, 1])  #añade varios elementos

mi_listas.remove(1.234)  #eliminar un valor de una lista para un valor char se usa "variable"

mi_listas2.pop()  #elimina e ultimo elemento de la lista

print(mi_listas[:])
print(mi_listas[1:3])#acceder a una porcion
print(mi_listas2[2])
print(mi_listas2[:])
print(mi_listas2.index("latina"))#muestra la pocicion en la que esta guardado el valor
print("sofai" in mi_listas2)#muestra si un valor se encuentra en una lista

mi_listas3 = mi_listas+mi_listas2
print(mi_listas3)
# imprimir solo los elementos mas grandes de una lista(arreglo de strings)
def solution(inputArray):
    m=[]
    for i in inputArray:
        m.append(len(i))
    count=max(m)
    l=[]
    for i in inputArray:
        if(len(i)==count):
            l.append(i)
    return l




