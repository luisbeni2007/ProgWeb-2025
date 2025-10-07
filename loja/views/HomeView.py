from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()

    if produto:
        produtos = produtos.filter(nome__icontains=produto)

    context = {
        'produtos': produtos
    }
    return render(request, 'home/home.html', context, status=200)
