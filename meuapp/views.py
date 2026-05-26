from django.shortcuts import render


def index(request):
    return render(request, "meuapp/index.html")


def elenco(request):

    personagens = [

        {
            "nome": "Mônica",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/monica.jpg"
        },

        {
            "nome": "Cebolinha",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/cebolinha.jpg"
        },

        {
            "nome": "Cascão",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/cascao.jpg"
        },

        {
            "nome": "Magali",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/magali.jpg"
        },

        {
            "nome": "Chico Bento",
            "idade": "10 anos",
            "origem": "Vila Abobrinha",
            "imagem": "imagens/chicobento.jpg"
        },

        {
            "nome": "Marina",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/marina.jpg"
        },

        {
            "nome": "Franjinha",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/franjinha.jpg"
        },

        {
            "nome": "Dorinha",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/dorinha.webp"
        },

        {
            "nome": "Xaveco",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/xaveco.png"
        },

        {
            "nome": "Do Contra",
            "idade": "10 anos",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/docontra.jpg"
        },

        {
            "nome": "Bidu",
            "idade": "Desconhecida",
            "origem": "Bairro do Limoeiro",
            "imagem": "imagens/bidu.jpg"
        }

    ]

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