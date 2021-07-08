from django.contrib import admin
from .models import Tipo_area,Sector,Area,Usuario_activo,Usuario,Actividad,Estatus_actividad,Turno,Registro_actividad

# Register your models here.
class Registro_actividadAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaRegistro',)
    #list_display = ('descripcion','idUsuario','fechaRegistro','idEstatusActividad')
    #fields = ['idUsuario','fechaRegistro','idEstatusActividad','fechaRegistro']


admin.site.register(Tipo_area)
admin.site.register(Sector)
admin.site.register(Area)
admin.site.register(Usuario_activo)
admin.site.register(Usuario)
admin.site.register(Actividad)
admin.site.register(Estatus_actividad)
admin.site.register(Turno)
admin.site.register(Registro_actividad,Registro_actividadAdmin)

