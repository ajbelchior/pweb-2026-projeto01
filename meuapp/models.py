from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=50)
    origem = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='personagens/')

    def __str__(self):
        return self.nome