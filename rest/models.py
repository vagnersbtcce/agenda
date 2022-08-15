'''
Modelo de Tarefa
Atributos:  - id: AUTO INCREMENT, PRIMARY KEY
            - descricao: VARCHAR(400)
            - criacao: DATE (preenchimento automático no criação)
            - categoria: VARCHAR(25), opções restritas, especificar no front-end
            - status: VARCHAR(25), opções restritas, especificar no front-end

A tabela Tarefa foi persistida no POSTGRESQL / Database: agenda (ver settings.py),
através da Biblioteca psycopg2-binary
'''

from django.db import models

# Classe Tarefa, herda classe Model do django.db.models
# Esta classe vai definir a tabela Tarefa quando os comandos forem executados:
# python manage.py makemigrations
# python manage.py migrate
class Tarefa(models.Model):

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=400, blank=True, default='')
    criacao = models.TimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, blank=True, default='importante')
    status = models.CharField(max_length=25, blank=True, default='Pendente')

    # Bloco abaixo nao eh necessario no funcionamento da API
    # Auxilia nos testes
    def __str__ (self):
        return '{}, {}, {}, {}'.format(self.id, self.descricao,
                                       self.criacao, self.categoria,
                                       self.status)

    def __repr__ (self):
        return '{}, {}, {}, {}'.format(self.id, self.descricao,
                                       self.criacao, self.categoria,
                                       self.status)
