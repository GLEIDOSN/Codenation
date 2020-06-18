from django.db import models
from django.core.validators import MinLengthValidator, validate_ipv4_address


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último Login', auto_now=True)
    email = models.EmailField('E-mail', max_length=254)
    password = models.CharField('Senha', max_length=50,
                                validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20, blank=True)
    version = models.CharField('Versão', max_length=5)
    address = models.GenericIPAddressField('Endereço de IP', max_length=39,
                                           validators=[validate_ipv4_address])

    def __str__(self):
        return self.name


class Event(models.Model):
    LEVEL_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('DEBUG', 'Debug'),
        ('ERROR', 'Error'),
        ('WARNING', 'Warning'),
        ('INFOR', 'Infor')
    ]
    level = models.CharField('level', max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField('Dados')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Data', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
