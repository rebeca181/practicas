from rest_framework import serializers
from .models import Cliente, Empleado, Menu, Factura

class clienteserializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class empleadoserializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class menuserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class facturaserializer(serializers.ModelSerializer):
    class Meta:
        model = Factura     
        fields = '__all__'
        