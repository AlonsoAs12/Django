from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto
from .models import Cliente


@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display=('nombre','pub_date')

@admin.register(Producto)
class Producto(admin.ModelAdmin):
    list_display=('nombre','precio','stock','pub_date')

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display=('nombres','apellidos','dni','telefono','email','fecha_nacimiento','fech_public')
