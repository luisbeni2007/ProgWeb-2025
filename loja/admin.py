from django.contrib import admin
from loja.models import Fabricante, Produto, Categoria

# Configuração para o modelo Fabricante
class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

# Configuração para o modelo Produto
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('nome', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria')
    empty_value_display = 'Vazio'

# Registro dos modelos no admin
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
#admin.site.register(Produto, ProdutoAdmin)
