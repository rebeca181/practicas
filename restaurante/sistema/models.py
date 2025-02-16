from django.core.validators import MinValueValidator, RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

# Validador para cédula ecuatoriana (10 dígitos)
def validar_cedula(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('La cédula debe tener exactamente 10 dígitos numéricos.')

# Validador para fechas (no se permiten fechas futuras)
def validar_fecha_no_futura(value):
    if value > date.today():
        raise ValidationError('La fecha no puede ser futura.')

# Validador para precio positivo
def validar_precio(value):
    if value <= 0:
        raise ValidationError('El precio debe ser mayor a cero.')

# Creamos la tabla de cliente   
class Cliente(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='Solo se permiten letras y espacios.')]
    )
    apellido = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='Solo se permiten letras y espacios.')]
    )
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='El número de teléfono debe tener 10 dígitos.')]
    )
    email = models.EmailField(validators=[EmailValidator(message='Ingrese un correo electrónico válido.')])
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
# Creamos la tabla de empleado
class Empleado(models.Model):
    cedula = models.CharField(
        max_length=10,
        validators=[validar_cedula]
    )
    nombre = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='Solo se permiten letras y espacios.')]
    )
    apellido = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='Solo se permiten letras y espacios.')]
    )
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='El número de teléfono debe tener 10 dígitos.')]
    )
    email = models.EmailField(validators=[EmailValidator(message='Ingrese un correo electrónico válido.')])
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"



# Validador para precio positivo
def validar_precio(value):
    if value <= 0:
        raise ValidationError('El precio debe ser mayor a cero.')

# Validador para fechas (no se permiten fechas futuras)
def validar_fecha_no_futura(value):
    if value > date.today():
        raise ValidationError('La fecha no puede ser futura.')

# Modelo Producto
class Menu(models.Model):
    menu = [
        ('almuerzo', 'Almuerzo'),
        ('cena', 'Cena'),
        ('desayuno', 'Desayuno')
    ]
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField(
        validators=[validar_precio]
    )
    
    def __str__(self):
        return self.descripcion
    
# Modelo Factura con cálculo automático del total
class Factura(models.Model):
    fecha = models.DateField(validators=[validar_fecha_no_futura])
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        validators=[MinValueValidator(1, message="La cantidad debe ser al menos 1.")]
    )
    total = models.FloatField(
        editable=False  # Desactiva la edición manual desde formularios
    )
    
    def save(self, *args, **kwargs):
        # Calculamos el total automáticamente antes de guardar
        if self.menu and self.cantidad:
            self.total = self.menu.precio * self.cantidad
        else:
            self.total = 0
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Factura del {self.fecha} - Cliente: {self.cliente.nombre} - Total: ${self.total:.2f}"
