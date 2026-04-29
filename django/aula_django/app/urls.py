from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('quem-somos', views.apresentacaoEquipe, name='quemsomos'),
    path('categoria', views.listarCategoria, name='categoria'),
    path('del-categoria/<int:id_cat>', views.delCategoria, name='delcategoria'),
    path('add-categoria', views.addCategoria, name="addcategoria"),
    path('edit-categoria/<int:id_cat>', views.editCategoria, name='editcategoria'),
    path('add-contato', views.addContato, name='addcontato'),
    path('listar-contatos', views.listarContatos, name='listarcontatos'),
    # path('edit-contato/<int:id_cont>', views.editContato, name='editcontato'),
    path('del-contato/<int:id_cont>', views.delContato, name='delcontato'),
    path('produtos', views.listarProdutos, name='produtos'),
    path('add-produto', views.addProduto, name='addproduto'),
    path('admin-produto', views.dashboardProdutos, name='adminproduto'),
    path('edit-produto/<int:id_prod>', views.editProduto, name='editproduto'),
    path('del-produto/<int:id_prod>', views.delProduto, name='delproduto'),
    path('criar-conta', views.criarConta, name='criarconta'),
    path('admin-usuarios', views.listarUsuarios, name='adminusuarios'),
    path('confirmacao/<classe>/<objeto>/<acao>/<id>', views.modalConfirmacao, name='modal')
]
