from neo4j import GraphDatabase
from icecream import ic

# Connection configurations for the Neo4j database
uri = "neo4j+s://2325c607.databases.neo4j.io"
username = "neo4j"
password = "egwgTosV6YfK-lfJaJTvYv09OIzpCCSd3UBpihAvbiE"


def run_query(query):
    """Executes a Cypher query in the Neo4j database."""
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        # Ensures the driver object is properly closed after execution
        with driver.session() as session:
            result = session.run(query)
            return result.data()


if __name__ == "__main__":
    # Query 1: Who in the family is an Engineer?
    query1 = "MATCH (p:Person {profession: 'Engineer'}) RETURN p.name AS Engenheiro"
    resultado1 = run_query(query1)
    nomes_engenheiros = [registro["Engenheiro"] for registro in resultado1]
    ic(nomes_engenheiros)

    # Query 2: Who are the children of Zé Galinha?
    query2 = "MATCH (ze_galinha:Person {name: 'Zé Galinha'})-[:FATHER_OF]->(filho) RETURN filho.name AS Filhos"
    resultado2 = run_query(query2)
    filhos_ze_galinha = [registro["Filhos"] for registro in resultado2]
    ic(filhos_ze_galinha)

    # Query 3: Who is Charleny's child?
    query3 = "MATCH (charleny:Person {name: 'Charleny Fonseca'})-[:MOTHER_OF]->(filho) RETURN filho.name AS Filhos"
    resultado3 = run_query(query3)
    filhos_charleny = [registro["Filhos"] for registro in resultado3]
    ic(filhos_charleny)

    # Query 4: What are the names of the family's pets and their owner?
    query4 = (
        "MATCH (p:Person)-[:OWNER_OF]->(pet:Pet) RETURN p.name AS Dono, pet.name AS Pet"
    )
    resultado4 = run_query(query4)
    donos_e_pets = [registro_pets for registro_pets in resultado4]
    ic(donos_e_pets)
