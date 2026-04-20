from django.shortcuts import render, redirect
from app.models import Categoria, Contato, Produto
from app.forms import FormCategoria, FormContato, FormProduto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listarCategoria(request):
    _categorias=Categoria.objects.all().values()
    return render(request, 'categoria.html', {'categorias':_categorias})

def delCategoria(request, id_cat):
    _categoria = Categoria.objects.get(id=id_cat)
    _categoria.delete()
    return redirect('categoria')

def addCategoria(request):
    formulario = FormCategoria(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')
    
    return render(request, 'add-categoria.html', {'form':formulario})

def editCategoria(request, id_cat):
    _categoria = Categoria.objects.get(id=id_cat)
    formulario = FormCategoria(request.POST or None, instance=_categoria)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')

    return render(request, 'edit-categoria.html', {'form': formulario})

def addContato(request):
    formulario = FormContato(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('listarcontatos')
    return render(request, 'contato.html', {'form': formulario})

def listarContatos(request):
    _contatos = Contato.objects.all().values()
    return render(request, 'admin-contatos.html', {'contatos': _contatos})

def editContato(request, id_cont):
    _contato = Contato.objects.get(id=id_cont)
    formulario = FormContato(request.POST or None, instance=_contato)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('listarcontatos')
    return render(request, 'edit-contato.html', {'form': formulario})

def delContato(request, id_cont):
    _contato = Contato.objects.get(id=id_cont)
    _contato.delete()
    return redirect('listarcontatos')

def addProduto(request):
    if request.method == 'POST':
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = FormProduto()

    return render(request, 'add-produto.html', {'form': form})

def listarProdutos(request):
    _produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': _produtos})

def editarProduto(request):
    pass