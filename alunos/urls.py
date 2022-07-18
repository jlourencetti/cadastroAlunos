from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:aluno_id>', views.ver_aluno, name='ver_aluno'),
]