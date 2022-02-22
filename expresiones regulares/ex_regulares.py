import re

cadena="vamos a aprender expresiones regulares la primera es buscar palabras en un texto aprender"
#print(re.search("aprender", cadena))#devuelve un objeto si lo encuentra y non si no lo encuentra
textoBusacar="aprender"
x=0
if re.search(textoBusacar, cadena) is not None:#solo encuentra 1
    x+=1
    print("e encontrado el texto ", x, " veces")
else:
    print("no e encontrado el texto")

print(len(re.findall(textoBusacar, cadena)))#len me ayuda aobtener el tamañp de la lista