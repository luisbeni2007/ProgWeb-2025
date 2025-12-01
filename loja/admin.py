from django.contrib import admin
from .models import *
#class FabricanteAdmin(admin.ModelAdmin):
#Conteudo da classe
admin.site.register(Fabricante)
admin.site.register(Categoria)
#class ProdutoAdmin(admin.ModelAdmin):
#Conteudo da classe
admin.site.register(Produto)
admin.site.register(Usuario)