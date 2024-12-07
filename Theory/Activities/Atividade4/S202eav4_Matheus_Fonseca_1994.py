###                           ##              ####
####                          ###              ####
###  ##########   ######## ########  #######   ####
####  ##### ####  ####  ####  ###   ####  #### ####
####  ###   ####   ########  ####  ########### ####
####  ####   #### ####  ####  ####  ####        ###
####  ###    ### ########### ###### ########## ####                 S202 - Banco de dados II
#### ####   ####  ##########  ####   ######    ###       Prof. Dr. Jonas Lopes de Vilas Boas

# Exercício Avaliativo 4 - Banco de dados orientado à colunas e Cassandra

"""
Estoque da Montadora

Um fabricante de automóveis contratou você para desenvolver um sistema de banco de dados distribuído usando o Cassandra para as linhas de montagem de toda a corporação, onde cada máquina pudesse acessar a base de dados e buscar as peças de maneira correta para ser montada nos respectivos modelos de veículos. Para isso, você deverá criar a tabela estoque no sistema DataStax ASTRA e inserir as colunas usando o arquivo auxiliar disponibilizado junto com essa atividade.

Questão 1: Siga os itens listados abaixo:

Faça a inserção de uma nova peça com os dados abaixo:

id: 5
nome: Pistao
carro: Mustang
estante: 4
nível: 1
quantidade: 167

Faça a inserção de uma nova peça com os dados abaixo:

id: 4
nome: Suspencao
carro: Argo
estante: 1
nível: 1
quantidade: 3500

Questão 2: Escreva o comando CQL utilizado para cada item abaixo:

Faça uma busca no banco de dados que retorno todos os dados do item com nome 'Pistão';
Faça uma busca no banco que calcule a média aritmética da quantidade de todas as colunas armazenadas na tabela;
Faça uma busca que retorne quantas colunas tem armazenadas na tabela;
Busque a maior e a menor quantidade de peças usando as alias "maior quantidade" e "menor quantidade" para a tabela estoque.
Faça uma busca que retorne os atributos nome, carro e quantidade, onde a estante seja igual a 3;
Faça uma busca que retorne a média aritmética da quantidade onde o nível seja igual a 1;
Faça uma busca retornando todos os atributos onde a estante seja menor do que 3 e o nível seja maior do que 4.


Questão 3: Elabore um script Python que seja capaz de fazer uma consulta mostrando nome, estante e quantidade do carro fornecido pelo usuário.

"""

import json

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory


class CassandraConnector:
    def __init__(self):
        self.cassandra_session = None

    def get_cassandra_connector(self):
        if self.cassandra_session is None:
            cloud_config = {"secure_connect_bundle": "secure-connect-exav.zip"}

            with open("ExAv-token.json") as f:
                secrets = json.load(f)

            CLIENT_ID = secrets["clientId"]
            CLIENT_SECRET = secrets["secret"]

            auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.cassandra_session = cluster.connect()
            self.cassandra_session.row_factory = dict_factory

            self.cassandra_session.set_keyspace("montadora")
        return self.cassandra_session


class AutoPart:
    def __init__(self, name, car, shelf, level, amount):
        self.name = name
        self.car = car
        self.shelf = shelf
        self.level = level
        self.amount = amount

    def to_dict(self):
        return {
            "name": self.name,
            "car": self.car,
            "shelf": self.shelf,
            "level": self.level,
            "amount": self.amount,
        }
    
    def to_touple(self):
        return (self.name, self.car, self.shelf, self.level, self.amount)


class AutoPartDAO:
    def __init__(self):
        self.cassandra_session = CassandraConnector().get_cassandra_connector()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS estoque (
            id int PRIMARY KEY,
            nome text,
            carro text,
            estante int,
            nivel int,
            quantidade int
        );
        """
        self.cassandra_session.execute(query)

    def add_part(self, auto_part):
        query = """
        INSERT INTO estoque (id, nome, carro, estante, nivel, quantidade)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        
        self.cassandra_session.prepare(query, auto_part.to_touple())

    def get_part(self, nome):
        query = "SELECT * FROM estoque WHERE nome = ? ALLOW FILTERING"
        prepared = self.cassandra_session.prepare(query)
        rows = self.cassandra_session.execute(prepared, [nome])
        return rows

    def get_average_amount(self):
        query = "SELECT AVG(quantidade) FROM estoque ALLOW FILTERING"
        rows = self.cassandra_session.execute(query)
        return rows

    def get_total_amount(self):
        query = "SELECT COUNT(*) FROM estoque ALLOW FILTERING"
        rows = self.cassandra_session.execute(query)
        return rows

    def get_max_min(self):
        query = "SELECT MAX(quantidade) AS maior_quantidade, MIN(quantidade) AS menor_quantidade FROM estoque ALLOW FILTERING"
        rows = self.cassandra_session.execute(query)
        return rows

    def get_parts_from_shelf(self, estante):
        query = "SELECT nome, carro, quantidade FROM estoque WHERE estante = ? ALLOW FILTERING"
        prepared = self.cassandra_session.prepare(query)
        rows = self.cassandra_session.execute(prepared, [estante])
        return rows

    def get_average_amount_from_level(self, nivel):
        query = "SELECT AVG(quantidade) FROM estoque WHERE nivel = ? ALLOW FILTERING"
        prepared = self.cassandra_session.prepare(query)
        rows = self.cassandra_session.execute(prepared, [nivel])
        return rows

    def get_parts_from_shelf_and_level(self, estante, nivel):
        query = "SELECT * FROM estoque WHERE estante < ? AND nivel > ? ALLOW FILTERING"
        prepared = self.cassandra_session.prepare(query)
        rows = self.cassandra_session.execute(prepared, [estante, nivel])
        return rows

    def get_parts_of_car(self, carro):
        query = "SELECT nome, estante, quantidade FROM estoque WHERE carro = ? ALLOW FILTERING"
        prepared = self.cassandra_session.prepare(query)
        rows = self.cassandra_session.execute(prepared, [carro])
        return rows


if __name__ == "__main__":
    part_dao = AutoPartDAO()
    part_dao.create_table()

    part1 = AutoPart("Pistao", "Mustang", 4, 1, 167)
    part2 = AutoPart("Suspencao", "Argo", 1, 1, 3500)

    part_dao.add_part(part1)
    part_dao.add_part(part2)

    print(part_dao.get_part("Pistao"))
    print(part_dao.get_average_amount())
    print(part_dao.get_total_amount())
    print(part_dao.get_max_min())
    print(part_dao.get_parts_from_shelf(3))
    print(part_dao.get_average_amount_from_level(1))
    print(part_dao.get_parts_from_shelf_and_level(3, 4))

    car = input("Digite o carro: ")
    print(part_dao.get_parts_of_car(car))
