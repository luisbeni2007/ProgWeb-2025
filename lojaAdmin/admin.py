from django.contrib import admin
from .models import *
class FabricanteAdmin(admin.ModelAdmin):
#Conteudo da classe
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
class ProdutoAdmin(admin.ModelAdmin):
#Conteudo da classe
admin.site.register(Produto, ProdutoAdmin)
# incluir a tabela de usuário no final
admin.site.register(Usuario)