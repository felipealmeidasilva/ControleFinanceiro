from django.db import models

# Create your models here.
class Cadastro(models.Model):
    TIPO_CHOICES = (
        ("Despesa", "Gasto"),
        ("Receita", "Receita"),
    )

    data = models.CharField(max_length=10)
    responsavel = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES, blank=False, null=False)
    valor = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data