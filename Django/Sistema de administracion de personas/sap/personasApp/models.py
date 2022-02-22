from django.db import models

class Domicilio(models.Model):
    calle=models.CharField(max_length=20)
    n_callees=models.IntegerField()
    pais=models.CharField(max_length=20)
    
class Personas (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    numero=models.IntegerField()
    categoria=models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'persona'
        verbose_name_plural ='personas'
        
    def __str__(self):
        return self.nombre