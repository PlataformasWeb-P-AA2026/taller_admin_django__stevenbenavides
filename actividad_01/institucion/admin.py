from django.contrib import admin
from .models import Museo, Guia_museo, Exposicion

class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion')
    search_fields = ('nombre', 'ciudad')

admin.site.register(Museo, MuseoAdmin)

class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia_guia', 'idiomas_hablados', 'museo')
    list_filter = ('museo',)
    search_fields = ('nombre_completo',)

admin.site.register(Guia_museo, GuiaMuseoAdmin)

class ExposicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'museo')
    list_filter = ('tematica',)
    search_fields = ('titulo_exhibicion',)

admin.site.register(Exposicion, ExposicionAdmin)