from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos_%Y%m%d', blank=True)

    def __str__(self):
        return self.nome_receita
