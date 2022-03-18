from django.contrib import admin
from .models import * # importa los modelos
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource (resources.ModelResource):
     class Meta:
         model = Categoria
         
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('nombre','estado')
    search_fields = ('nombre',)
    resources_class=CategoriaResource

class AutorAdmin(admin.ModelAdmin):
    list_display=('nombres','apellido','estado')
    search_fields = ('nombres','apellido')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post)
