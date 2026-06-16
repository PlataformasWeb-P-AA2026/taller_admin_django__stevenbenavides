from django.contrib import admin
from .models import Museo, Guia_museo, Exposicion

class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion', 'mejor_guia')
    search_fields = ('nombre', 'ciudad')

    def mejor_guia (self, obj):
        guia_top = obj.guias.order_by('-anios_experiencia_guia').first()
        if guia_top:
            return f"{guia_top.nombre_completo} ({guia_top.anios_experiencia_guia} años)"
        return "Sin guías asignados"
    mejor_guia.short_description = 'Guía con Más Experiencia'

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