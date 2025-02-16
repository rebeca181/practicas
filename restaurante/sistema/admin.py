from django.contrib import admin

from .models import Cliente, Empleado, Menu, Factura

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Menu)
admin.site.register(Factura)
