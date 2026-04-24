from django.shortcuts import render, redirect
from app.models import Categoria, Contato, Produto
from app.forms import FormCategoria, FormContato, FormProduto, FormUsuario
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def apresentacaoEquipe(request):
    return render(request, 'apresentacao-equipe.html')

def listarCategoria(request):
    _categorias=Categoria.objects.all().values()
    return render(request, 'categoria/categoria.html', {'categorias':_categorias})

def delCategoria(id_cat):
    _categoria = Categoria.objects.get(id=id_cat)
    _categoria.delete()
    return redirect('categoria')

def addCategoria(request):
    formulario = FormCategoria(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')
    
    return render(request, 'categoria/add-categoria.html', {'form':formulario})

def editCategoria(request, id_cat):
    _categoria = Categoria.objects.get(id=id_cat)
    formulario = FormCategoria(request.POST or None, instance=_categoria)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')

    return render(request, 'categoria/edit-categoria.html', {'form': formulario})

def addContato(request):
    formulario = FormContato(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('listarcontatos')
    return render(request, 'contato/contato.html', {'form': formulario})

def listarContatos(request):
    _contatos = Contato.objects.all().values()
    return render(request, 'admin/admin-contatos.html', {'contatos': _contatos})

def editContato(request, id_cont):
    _contato = Contato.objects.get(id=id_cont)
    formulario = FormContato(request.POST or None, instance=_contato)

    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('listarcontatos')
    return render(request, 'contato/edit-contato.html', {'form': formulario})

# def delContato(request, id_cont):
#     _contato = Contato.objects.get(id=id_cont)
#     _contato.delete()
#     return redirect('listarcontatos')

def addProduto(request):
    if request.method == 'POST':
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = FormProduto()

    return render(request, 'produto/add-produto.html', {'form': form})

def dashboardProdutos(request):
    _produtos = Produto.objects.all()
    return render(request, 'admin/admin-produtos.html', {'produtos': _produtos})

def listarProdutos(request):
    _produtos = Produto.objects.all()
    return render(request, 'produto/produtos.html', {'produtos': _produtos})

def editProduto(request, id_prod):
    _produto = Produto.objects.get(id=id_prod)
    form = FormProduto(request.POST or None, request.FILES, instance=_produto)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('adminproduto')
    else:
        form = FormProduto(instance=_produto)

    return render(request, 'produto/edit-produto.html', {'form': form})

def delProduto(request, id_prod):
    _produto = Produto.objects.get(id=id_prod)
    _produto.delete()
    return redirect('adminproduto')

def criarConta(request):
    form = FormUsuario(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'criar-conta.html', {'form': form})

def listarUsuarios(request):
    _usuarios = User.objects.all()
    return render(request, 'admin/admin-usuarios.html', {'usuarios': _usuarios})