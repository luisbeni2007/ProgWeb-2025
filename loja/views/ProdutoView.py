from django.shortcuts import render, redirect
from loja.models import Produto, Fabricante, Categoria
from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

# A FUNÇÃO PRODUTO_VIEW (CRIAR PRODUTO)
def list_produto_view(request, id=None):
    # Processa o post ou gerada pela action
    if request.method == 'POST':
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        preco = request.POST.get("preco")
        image = request.FILES.get("image")
        
        # Adiciona Fabricante e Categoria do POST
        categoria_id = request.POST.get("CategoriaFk")
        fabricante_id = request.POST.get("FabricanteFk")
        
        print("postback-create")
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        print(preco)
        print(image)
        try:
            obj_produto = Produto()
            obj_produto.produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
                
            obj_produto.preco = 0
            if (preco is not None) and (preco != ""):
                obj_produto.preco = preco

            # Salva as chaves estrangeiras (FKs) no objeto de criação
            if fabricante_id and int(fabricante_id) > 0:
                obj_produto.fabricante = Fabricante.objects.filter(id=fabricante_id).first()
            if categoria_id and int(categoria_id) > 0:
                obj_produto.categoria = Categoria.objects.filter(id=categoria_id).first()

            obj_produto.criado_em = timezone.now()
            obj_produto.alterado_em = obj_produto.criado_em
            
            # Se for anexado arquivo, salva na pasta e guarda nome no objeto
            if request.FILES is not None:
                num_files = len(request.FILES.getlist('image'))
                if num_files > 0:
                    imagefile = request.FILES['image']
                    print(imagefile)
                    fs = FileSystemStorage()
                    filename = fs.save(imagefile.name, imagefile)
                    if (filename is not None) and (filename != ""):
                        obj_produto.image = filename
                        
            obj_produto.save()
            print("Produto %s salvo com sucesso" % produto)
            
            # Redireciona para o formulário de criação após o sucesso
            return redirect('produto') # Assume 'produto' é a URL da lista/criação
        except Exception as e:
            print("Erro inserindo produto: %s" % e)
            
    # Adicionei os Fabricantes e Categorias aqui para que o formulário de criação possa usá-los (SELECTs)
    Fabricantes = Fabricante.objects.all()
    Categorias = Categoria.objects.all()
    context = {'fabricantes' : Fabricantes, 'categorias' : Categorias}
            
    return render(request, template_name='produto/produto-create.html', context=context, status=200)


@login_required
# Até aqui
def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    
    # adicione a lista de fabricantes e categorias no context
    Fabricantes = Fabricante.objects.all()
    Categorias = Categoria.objects.all()
    
    context = {'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='produto/produto-edit.html', context=context, status=200)

# A FUNÇÃO EDIT_PRODUTO_POSTBACK (SALVAR EDIÇÃO)
def edit_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto = request.POST.get("produto") # Mudança de 'Produto' para 'produto' para consistência
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        
        # Adicionado o campo preco
        preco = request.POST.get("preco")
        
        # adicione a requisição do valor do campo post
        categoria = request.POST.get("CategoriaFk")
        fabricante = request.POST.get("FabricanteFk")
        
        # Adicionado o campo de imagem (se houver upload)
        image = request.FILES.get("image")
        
        print("postback-edit")
        print(f"ID: {id}")
        print(f"Produto: {produto}")
        
        try:
            # Busca o produto existente
            obj_produto = Produto.objects.filter(id=id).first()
            
            # Se o produto for encontrado, atualiza os campos
            if obj_produto:
                obj_produto.produto = produto
                obj_produto.destaque = (destaque is not None)
                obj_produto.promocao = (promocao is not None)

                # Atualiza o preço
                obj_produto.preco = 0
                if (preco is not None) and (preco != ""):
                    obj_produto.preco = preco
                    
                # Salva os objetos fabricante e categoria filtrados com base no id
                if fabricante and int(fabricante) > 0:
                    obj_produto.fabricante = Fabricante.objects.filter(id=fabricante).first()
                else:
                    obj_produto.fabricante = None # Define como None se for a opção default/vazia
                    
                if categoria and int(categoria) > 0:
                    obj_produto.categoria = Categoria.objects.filter(id=categoria).first()
                else:
                    obj_produto.categoria = None # Define como None se for a opção default/vazia

                if msgPromocao is not None:
                    obj_produto.msgPromocao = msgPromocao
                
                # Trata a atualização da imagem
                if image:
                    print(f"Nova imagem anexada: {image}")
                    fs = FileSystemStorage()
                    filename = fs.save(image.name, image)
                    if (filename is not None) and (filename != ""):
                        obj_produto.image = filename
                
                # Atualiza a data de alteração
                obj_produto.alterado_em = timezone.now()
                
                obj_produto.save()
                
                print(f"Produto {produto} atualizado com sucesso!")
                
                # Redireciona para a lista de produtos
                return redirect('produto')
            else:
                print(f"Produto com ID {id} não encontrado.")
                return redirect('produto') # Redireciona para a lista em caso de ID inválido
        
        except Exception as e:
            print(f"Erro atualizando produto: {e}")
            # Em caso de erro, redireciona de volta para a edição com o ID
            return redirect(f'/produto/edit/{id}')
            
    # Se for um GET (ou outra requisição), redireciona para a lista
    return redirect('produto')
    