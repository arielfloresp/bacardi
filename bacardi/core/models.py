from django.db import models

class Continente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.CharField(max_length=255)

    def __str__(self):
        return self.imagen


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    botellas_tomadas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_promocion = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre_promocion


class Participacion(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    es_mayor_de_edad = models.BooleanField()
    cantidad_botellas = models.IntegerField()
    fecha_participacion = models.DateTimeField()

    def __str__(self):
        return f"Participacion de {self.persona} en {self.promocion}"
