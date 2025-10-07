from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = (
        'Produto',
        'destaque',
        'promocao',
        'msgPromocao',
        'preco',
        'categoria',
    )
    empty_value_display = 'Vazio'

# Registrar o modelo no admin
admin.site.register(Produto, ProdutoAdmin)