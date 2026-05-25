from django.shortcuts import render


# =========================
# PÁGINA INICIAL
# =========================

def index(request):

    dados = {
        'titulo1': 'BEM VINDO AO',

        'titulo2': 'MUNDO DA DIVERSÃO!',

        'descricao': 'A Turma da Mônica é uma das séries de quadrinhos mais famosas do Brasil, criada por Maurício de Sousa em 1959. As histórias acompanham as aventuras de Mônica, Cebolinha, Cascão, Magali e seus amigos no Bairro do Limoeiro.'
    }

    return render(request, 'meuapp/index.html', dados)


# =========================
# ELENCO
# =========================

def elenco(request):

    personagens = [

    {
        'nome': 'Mônica',
        'idade': 10,
        'posicao': 'Líder da turma',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/monica.jpg'
        },

    {
        'nome': 'Cebolinha',
        'idade': 10,
        'posicao': 'Criador de planos infalíveis',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/cebolinha.jpg'
    },

    {
        'nome': 'Cascão',
        'idade': 10,
        'posicao': 'Melhor amigo do Cebolinha',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/cascao.jpg'
    },

    {
        'nome': 'Magali',
        'idade': 10,
         'posicao': 'Comilona da turma',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/magali.jpg'
    },

    {
        'nome': 'Chico Bento',
        'idade': 10,
        'posicao': 'Menino da roça',
        'origem': 'Vila Abobrinha',
        'foto': 'imagens/chicobento.jpg'
    },

    {
        'nome': 'Marina',
        'idade': 10,
        'posicao': 'Artista da turma',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/marina.jpg'
    },

    {
        'nome': 'Franjinha',
        'idade': 10,
        'posicao': 'Inventor e cientista',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/franjinha.jpg'
    },

    {
        'nome': 'Dorinha',
        'idade': 10,
        'posicao': 'Amiga aventureira',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/dorinha.webp'
    },

    {
        'nome': 'Xaveco',
        'idade': 10,
        'posicao': 'Amigo engraçado',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/xaveco.png'
    },

    {
        'nome': 'Do Contra',
        'idade': 10,
        'posicao': 'Garoto do contra',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/docontra.jpg'
    },

    {
        'nome': 'Bidu',
        'idade': 5,
        'posicao': 'Mascote da turma',
        'origem': 'Bairro do Limoeiro',
        'foto': 'imagens/bidu.jpg'
    }

    ]

    return render(request, 'meuapp/elenco.html', {
        'personagens': personagens
    })


# =========================
# SOBRE
# =========================

def sobre(request):

    info = {
        'tecnologias': 'Django, HTML e CSS',
        'autor': 'Ana Júlia C. Belchior'
    }

    return render(request, 'meuapp/sobre.html', info)