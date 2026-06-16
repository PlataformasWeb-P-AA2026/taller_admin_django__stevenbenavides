from django.contrib import admin
from django.db.models import Max, Sum
from .models import Museo, Guia_museo, Exposicion

class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion', 'costo_total_produccion', 'guias_exp')
    search_fields = ('nombre', 'ciudad')

    def costo_total_produccion(self, obj):
        total = obj.guias.aggregate(total_costo=Sum('exposiciones__costo_produccion'))['total_costo']
        if total:
            return f"{total}"
        return "0.00"
    
    costo_total_produccion.short_description = 'Costo Total Producción'


    def guias_exp(self, obj):
        max_exp = obj.guias.aggregate(maximo=Max('anios_experiencia_guia'))['maximo']
        
        if max_exp is not None:
            mejores_guias = obj.guias.filter(anios_experiencia_guia=max_exp)
            nombres = [guia.nombre_completo for guia in mejores_guias]
            return f"{', '.join(nombres)}"
    
    guias_exp.short_description = 'Guia(s) con Mas Experiencia'

admin.site.register(Museo, MuseoAdmin)


class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia_guia', 'idiomas_hablados', 'museo')
    list_filter = ('museo',)
    search_fields = ('nombre_completo',)

admin.site.register(Guia_museo, GuiaMuseoAdmin)


class ExposicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'nombre_museo')
    list_filter = ('tematica',)
    search_fields = ('titulo_exhibicion',)

    def nombre_museo(self, obj):
        if obj.museo and obj.museo.museo:
            return obj.museo.museo.nombre
        return "Sin museo"
    
    nombre_museo.short_description = 'Museo'

admin.site.register(Exposicion, ExposicionAdmin)