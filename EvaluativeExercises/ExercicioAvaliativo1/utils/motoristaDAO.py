from bson.objectid import ObjectId
from classes.motorista import Motorista


class MotoristaDAO:
    def __init__(self, database):
        """
        Initialize the MotoristaDAO with a database connection.

        Args:
            database (DatabaseConnection): The database connection object to be used for database operations.
        """
        self.db = database

    def create(self, motorista: Motorista):
        """
        Inserts a new Motorista document into the database.

        Args:
            motorista (Motorista): An instance of the Motorista class containing the data to be inserted.

        Returns:
            ObjectId: The ID of the inserted Motorista document if the operation is successful.
            None: If an error occurs during the insertion process.

        Raises:
            Exception: If an error occurs during the insertion process, it will be caught and printed.
        """
        try:
            res = self.db.collection.insert_one(vars(motorista))
            print(f"Motorista criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read(self, id: str):
        """
        Retrieve a motorista document from the database by its ID.

        Args:
            id (str): The ID of the motorista document to retrieve.

        Returns:
            dict: The motorista document if found, otherwise None.

        Raises:
            Exception: If an error occurs during the database operation.
        """
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update(self, id: str, novas_corridas: list):
        """
        Updates the motorista document in the MongoDB collection with new rides and recalculates the average rating.
        Args:
            id (str): The unique identifier of the motorista document to update.
            novas_corridas (list): A list of new rides to be added to the motorista's existing rides.
        Returns:
            int: The number of documents modified in the MongoDB collection.
            None: If the motorista is not found or an error occurs during the update process.
        Raises:
            Exception: If an error occurs while updating the motorista document.
        """
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(id)})
            if motorista:
                motorista["corridas"].extend(novas_corridas)

                notas = [corrida["nota"] for corrida in motorista["corridas"]]
                motorista["nota"] = sum(notas) / len(notas)

                res = self.db.collection.update_one(
                    {"_id": ObjectId(id)}, {"$set": motorista}
                )
                print(
                    f"Motorista atualizado: {res.modified_count} documento(s) atualizado(s)"
                )
                return res.modified_count
            else:
                print("Motorista não encontrado.")
                return None
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete(self, id: str):
        """
        Deletes a motorista document from the database by its ID.

        Args:
            id (str): The ID of the motorista document to delete.

        Returns:
            int: The number of documents deleted (should be 1 if successful, 0 if no document was found).
            None: If an exception occurred during the deletion process.

        Raises:
            Exception: If an error occurs during the deletion process, it will be caught and printed.
        """
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None
