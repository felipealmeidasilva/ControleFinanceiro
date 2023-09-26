from django.db import models

# Create your models here.
class Cadastro(models.Model):

    data = models.CharField(max_length=10)
    responsavel = models.CharField(max_length=50)
    descricao = models.TextField()
    tipo = models.CharField(max_length=7)
    valor = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data