from django.urls import path
from . import views

urlpatterns = [
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]