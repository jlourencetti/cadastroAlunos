from django.shortcuts import render
from .models import Aluno
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    alunos = Aluno.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)
    return render(request, 'alunos/index.html', {
        'alunos': alunos
    })


def ver_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    return render(request, 'alunos/ver_aluno.html', {
        'aluno': aluno
    })


def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    alunos = Aluno.objects.annotate(nome_completo=campos).filter(nome_completo__icontains=termo)
    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)
    return render(request, 'alunos/busca.html', {
        'alunos': alunos
    })
