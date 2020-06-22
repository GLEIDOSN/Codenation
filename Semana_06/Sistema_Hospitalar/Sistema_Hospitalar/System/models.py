from tkinter import CASCADE
from django.db import models


class Tipo_Instituicao(models.Model):
    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.nome


class Municipios(models.Model):
    cod_municipio = models.CharField('Código', max_length=5)
    nome = models.CharField('Município', max_length=60)
    UF = models.CharField('UF', max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.UF}"


class Instituicoes(models.Model):
    STATUS_CHOICES = [('A', 'Ativo'), ('I', 'Inativo')]
    tipo = models.ForeignKey(Tipo_Instituicao, on_delete=models.DO_NOTHING)
    razao_social = models.CharField('Razão Social', max_length=120)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=120)
    CNPJ = models.CharField('CNPJ', max_length=14)
    inscricao_estadual = models.CharField('I.E', max_length=30, blank=True)
    inscricao_municipal = models.CharField('I.M', max_length=30, blank=True)
    numero_CNAE = models.IntegerField('Numero CNAE')
    logradouro = models.CharField('Endereço', max_length=120, blank=True)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=50)
    CEP = models.CharField('CEP', max_length=8)
    municipios = models.ForeignKey(Municipios, on_delete=models.DO_NOTHING)
    UF = models.CharField('UF', max_length=2)
    complemento = models.CharField('Complemento', max_length=250)
    diretor_geral = models.CharField('Diretor Geral', max_length=120)
    diretor_administrativo = models.CharField('Diretor Administrativo', max_length=120)
    diretor_financeiro = models.CharField('Diretor Financeiro', max_length=120)
    telefone_emergencia = models.CharField('Fone Emergencia: ', max_length=11)
    ramal_emergencia = models.CharField('Ramal Emergência', max_length=11)
    celular_emergencia = models.CharField('Celular Emergência', max_length=11)
    telefone_ambulatorio = models.CharField('Celular Emergência', max_length=11)
    ramal_ambulatorio = models.CharField('Ramal Ambulatório', max_length=11)
    celular_ambulatorio = models.CharField('Celular Ambulatório', max_length=11)
    telefone_centro_cirurgico = models.CharField('Tel. Centro Cirúrgico', max_length=11)
    ram_centro_cirurgico = models.CharField('Ramal C. Cirúrgico', max_length=11)
    celular_centro_cirurgico = models.CharField('Celular C. Cirúrgico', max_length=11)
    telefone_geral = models.CharField('Telefone Geral', max_length=11)
    celular_geral = models.CharField('Celular Geral', max_length=11)
    status = models.CharField('status', max_length=1, choices=STATUS_CHOICES)
