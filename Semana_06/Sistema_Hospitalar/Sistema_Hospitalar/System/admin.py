from django.contrib import admin
from System.models import Tipo_Instituicao, Instituicoes, Municipios


class ModelAdmin_Instituicoes(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'CNPJ')


class ModelAdmin_Tipo_Instituicao(admin.ModelAdmin):
    list_display = ('id', 'nome')


class ModelAdmin_Municipios(admin.ModelAdmin):
    list_display = ('id', 'cod_municipio', 'nome')


admin.site.register(Tipo_Instituicao, ModelAdmin_Tipo_Instituicao)
admin.site.register(Instituicoes, ModelAdmin_Instituicoes)
admin.site.register(Municipios, ModelAdmin_Municipios)
