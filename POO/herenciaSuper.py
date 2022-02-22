class persona():
    def __init__(self, nombres, edades, Lugar_residencia):
        self.nombre=nombres
        self.edad=edades
        self.lugar=Lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre,"\nEdad: ", self.edad,"\nLugar de residencia: ", self.lugar)

class empleado(persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, recidencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, recidencia_empleado) #super inicia el metodo init de la clase init y le envai los datos
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario", self.salario, "\nAntiguedad" ,self.antiguedad)

datos=empleado(1500,53,"juan",55,"colombia")

datos.descripcion()

print(isinstance(datos,empleado))#nos muestra si una instancia pertenece a una clase
