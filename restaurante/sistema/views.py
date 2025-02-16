from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Cliente, Empleado, Menu, Factura
from sistema.serializer import clienteserializer, empleadoserializer, menuserializer, facturaserializer
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = clienteserializer
    permission_classes = [AllowAny]
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = empleadoserializer
    permission_classes = [AllowAny]
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = menuserializer
    permission_classes = [AllowAny]

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = facturaserializer
    permission_classes = [AllowAny]