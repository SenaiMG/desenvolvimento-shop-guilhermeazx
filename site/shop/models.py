import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime
from django.db import models

# Create your models here.

class Site (models.Model):
    nome_card = models.CharField(max_length = 200)
    description = models.TextField()
    path = models.ImageField()
    primeiro_texto = models.TextField()
    segundo_texto = models.TextField()
    alunos = models.IntegerField()
    date_create = models.DateTimeField(default = datetime.now, blank = True)

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user= user_name,
            passwd = user_password    
        )
        print('conectado com sucesso')
    except Error as err:
        print('erro')
    return connection


class ItensEstoque:
    nome : str
    preco : float
    quantidade : int

    def ganho_total(self) ->float:
        return self.preco * self.quantidade

    def __init__(self, name: str, preco: float, quantidade : int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade