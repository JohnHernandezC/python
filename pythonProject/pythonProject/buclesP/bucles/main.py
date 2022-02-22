imprimir=["maria","juamita","latina","morenita",1,2,3,4]

for i in [1,2,3]: #o ["maria","juamita","latina","morenita"]
    print("hola putos")

    print("hola putos", end=" ")
    print(imprimir)


email=False
mi_email=input("introduce tu email")
for i in mi_email:
    print("putos", end=" ")
    if(i=="@"):
     email=True

if(email==True):
       print("es un correo")
else:
       print("no es un corrreo")


