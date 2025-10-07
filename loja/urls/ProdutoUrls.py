from django.urls import path
from loja.views.ProdutoView import list_produto_view, edit_produto_view, edit_produto_postback
 #, details_produto_view, delete_produto_view,create_produto_view


urlpatterns = [
    path("", list_produto_view, name= 'produto'),
    path("<int:id>", list_produto_view, name= 'produto_com_id'), # Ajustei o nome para evitar conflito
    path("edit/<int:id>", edit_produto_view, name= 'edit_produto'),
    path("edit", edit_produto_postback, name= 'edit_produto_postback'),
 #   path("details/<int:id>", details_produto_view, name= 'details_produto'),
   # path("delete/<int:id>", delete_produto_view, name= 'delete_produto'),
    #path("create", create_produto_view, name= 'create_produto'),
]