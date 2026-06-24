from django.shortcuts import render
from .models import Personagem

def index(request):
    return render(request, "meuapp/index.html")


def elenco(request):
    personagens = Personagem.objects.all()

    context = {
        "personagens": personagens
    }

    return render(
        request,
        "meuapp/elenco.html",
        context
    )


def sobre(request):
    return render(request, "meuapp/sobre.html")