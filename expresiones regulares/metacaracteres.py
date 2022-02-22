import re
#encontrar coincidencias en el principio o el fin
listaNombres=["ana gomez niño","maria martin","sandra lopez niña","sandra nuñes", "santiago martin","niños","niñas"]

for i in listaNombres:
    if re.findall('^sandra',i):# el meta caracter es ^
        print(i)
for i in listaNombres:
    if re.findall('martin$',i):# el meta caracter es $
        print(i)

for i in listaNombres:
    if re.findall('[ñ]',i):# el meta caracter es [] si queremos buscar en un rango podemos usar [o-t]
        print(i)
print("--------------------------------------------------")
for i in listaNombres:
    if re.findall('niñ[oa]s',i):# el meta caracter es 
        print(i)