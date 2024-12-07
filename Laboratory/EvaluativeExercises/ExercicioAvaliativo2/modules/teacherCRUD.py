class TeacherCRUD:
    def __init__(self, db):
        """
        Initialize the TeacherCRUD instance with a database connection.

        Args:
            db: The database connection object.

        """
        self.db = db

    def create(self, name, ano_nasc, cpf):
        """
        Creates a new Teacher node in the database with the given attributes.

        Args:
            name (str): The name of the teacher.
            ano_nasc (int): The year of birth of the teacher.
            cpf (str): The CPF (Cadastro de Pessoas Físicas) of the teacher.

        Side Effects:
            Executes a query to create a new Teacher node in the database.
        """
        query = f"CREATE(:Teacher{{name:'{name}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})"
        self.db.execute_query(query)

    def read(self, name):
        """
        Retrieves teacher records from the database by name.

        Args:
            name (str): The name of the teacher to search for.

        Returns:
            list: A list of teacher records that match the given name.

        Side Effects:
            Executes a query on the database to retrieve the teacher records.
        """
        query = f"MATCH(t:Teacher{{name:'{name}'}}) RETURN t"
        result = self.db.execute_query(query)
        return [record["t"] for record in result]

    def delete(self, name):
        """
        Deletes a teacher node from the database based on the provided name.

        Args:
            name (str): The name of the teacher to be deleted.

        Side Effects:
            Executes a query to delete the teacher node from the database.
        """
        query = f"MATCH(t:Teacher{{name:'{name}'}}) DETACH DELETE t"
        self.db.execute_query(query)

    def update(self, name, new_cpf):
        """
        Updates the CPF of a teacher in the database.

        Args:
            name (str): The name of the teacher whose CPF is to be updated.
            new_cpf (str): The new CPF value to be set for the teacher.

        Side Effects:
            Executes a query on the database to update the teacher's CPF.
        """
        query = f"MATCH(t:Teacher{{name:'{name}'}}) SET t.cpf = '{new_cpf}'"
        self.db.execute_query(query)
