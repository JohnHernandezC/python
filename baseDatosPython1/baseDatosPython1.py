import sqlite3

miConexion=sqlite3.connect("base de datos CON PK")
miCursor=miConexion.cursor()

#solo se ejecuta para crear una tabla (LAS TRES COMILLAS ES PARA PODER DIVIDIR EL CODIGO EN VARIAS LINEAS)
#agregamos la primary key Y AUTOINCREMENT AYUDA AQUE EL VALOR SE VAYA INCREMENTANDO SOLO
#LA CLAPSULA UNIQUE SIRVE PRA QUE SOLO SE PUEDA INSERTAR UN TIPO DE DATO EJEMPLO UN SOLO NUMERO DE CEDULA POR BASE DE DATOS
#miCursor.execute('''CREATE TABLE productos_dos (
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 Nombre_articulo VARCHAR(50) UNIQUE, 
#                 precio INTEGER, 
#                 seccion VARCHAR(50))''')

#INSERTAR UN DATO
#miCursor.execute("INSERT INTO productos VALUES('BALON',15,'DEPORTES')")
#miConexion.commit()

#-------------------------------------------------------------------------------------------------------
#INSERTAR varios DATOs
#productosvarios=[
#    ("camiseta",10,"deportes"),
#    ("jarron",90,"seramica"),
#    ("camion",100,"juguetes"),
#    ("MUÑECA",10,"juguetes")
    
#    ]
#miCursor.executemany("INSERT INTO productos_dos VALUES (NULL,?,?,?)",productosvarios)# los interrogantes son el numero filas a insertar Y NULL ES PRA EL ESPACIO PARA AUTOINCREMENTO
#miConexion.commit()
#-------------------------------------------------------------------
#VER DATOS GUARDADOS EN LA BASE
#miCursor.execute("SELECT * FROM productos_dos")

#varios=miCursor.fetchall()# esto trae todos los datos en forma de lista
#print(varios)
#for pro in varios:
 #   print(pro[0])# podemos filtrar por columna POR EJEMPLO AQUI SOLO MUESTRA  NOMBRE

#--------------------------------------------------------------------------
#BUSCAR POR DATOS ESPESIFICOS
#miCursor.execute("SELECT * FROM productos_dos WHERE seccion='juguetes'")
#varios=miCursor.fetchall()# esto trae todos los datos en forma de lista
#print(varios)

#--------------------------------------------------------------------------
#UPDATE

miCursor.execute("UPDATE productos_dos SET precio=222 WHERE nombre_articulo='camiseta'")
miConexion.commit()

#--------------------------------------------------------------------------
#DELETE
miCursor.execute("DELETE FROM productos_dos WHERE ID=3")
miConexion.commit()


miConexion.close()