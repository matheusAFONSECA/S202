from neo4j import GraphDatabase


class Database:
    """
    A class used to represent a connection to a Neo4j database.
    Methods
    -------
    __init__(uri, user, password)
        Initializes the database connection with the given URI, user, and password.
    close()
        Closes the database connection.
    execute_query(query, parameters=None)
        Executes a given Cypher query with optional parameters and returns the results.
    drop_all()
        Deletes all nodes and relationships in the database.
    """

    def __init__(self, uri, user, password):
        """
        Initializes the Database instance with the given URI, user, and password.
        Parameters
        ----------
        uri : str
            The URI of the Neo4j database.
        user : str
            The username for authentication.
        password : str
            The password for authentication.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """
        Closes the database connection.
        """
        self.driver.close()

    def execute_query(self, query, parameters=None):
        """
        Executes a given Cypher query with optional parameters and returns the results.
        Parameters
        ----------
        query : str
            The Cypher query to be executed.
        parameters : dict, optional
            A dictionary of parameters to be used in the query (default is None).
        Returns
        -------
        list
            A list of records returned by the query.
        """
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

    def drop_all(self):
        """
        Deletes all nodes and relationships in the database.
        """
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
