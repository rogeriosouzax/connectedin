from django.shortcuts import render, redirect
# caso queira retornar uma código html diretamente na minha função
from django.http import HttpResponse
from perfis.models import Perfil, Convite

def index(request):
    return render(request, 'index.htm', {'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})
    # return HttpResponse('<h2>Bem vindo ao meu site!</h2>')

def exibir(request, perfil_id):
    
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()

    return render(request, 'perfil.htm', {'perfil' : perfil, 'ja_eh_contato' : ja_eh_contato})

def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')

def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()

    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)