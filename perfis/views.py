from django.shortcuts import render, redirect
# caso queira retornar uma código html diretamente na minha função
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.htm', {'perfis' : Perfil.objects.all()})
    # return HttpResponse('<h2>Bem vindo ao meu site!</h2>')

def exibir(request, perfil_id):
    
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.htm', {'perfil' : perfil})

def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)