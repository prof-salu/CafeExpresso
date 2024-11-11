from django.db import models


class Filial(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.endereco)

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiais'

