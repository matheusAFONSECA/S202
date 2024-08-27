from dataset.pokemon_dataset import dataset
import pymongo  # pip install pymongo


class Database:
    def __init__(self, database, collection):
        """
        Initializes a Database object.

        Args:
            database (str): The name of the MongoDB database.
            collection (str): The name of the collection within the database.
        """
        self.connect(database, collection)

    def connect(self, database, collection):
        """
        Connects to the MongoDB database and collection.

        Args:
            database (str): The name of the MongoDB database.
            collection (str): The name of the collection within the database.
        """
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString, tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Connected to the database successfully!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        """
        Resets the database by dropping the collection and inserting new data.
        """
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Database reset successfully!")
        except Exception as e:
            print(e)
