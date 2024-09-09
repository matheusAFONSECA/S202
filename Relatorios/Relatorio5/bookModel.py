from bson.objectid import ObjectId


class BookModel:
    """
    A model for managing book data in a database.

    Attributes:
        db (Database): An instance of the Database class to interact with.
    """

    def __init__(self, database):
        """
        Initializes the BookModel with the given database.

        Args:
            database (Database): An instance of the Database class to interact with.
        """
        self.db = database

    def create_book(self, title: str, author: str, year: int, price: float):
        """
        Creates a new book entry in the database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year of publication.
            price (float): The price of the book.

        Returns:
            ObjectId: The ID of the created book if successful, otherwise None.
        """
        try:
            res = self.db.collection.insert_one(
                {"titulo": title, "autor": author, "ano": year, "preco": price}
            )
            print(f"Book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating the book: {e}")
            return None

    def read_book_by_id(self, id: str):
        """
        Retrieves a book entry from the database by its ID.

        Args:
            id (str): The ID of the book to retrieve.

        Returns:
            dict or None: The book data if found, otherwise None.
        """
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            if res:
                print(f"Book found: {res}")
            else:
                print("No book found with that ID.")
            return res
        except Exception as e:
            print(f"An error occurred while reading the book: {e}")
            return None

    def update_book(self, id: str, title: str, author: str, year: int, price: float):
        """
        Updates an existing book entry in the database.

        Args:
            id (str): The ID of the book to update.
            title (str): The new title of the book.
            author (str): The new author of the book.
            year (int): The new year of publication.
            price (float): The new price of the book.

        Returns:
            int or None: The number of documents modified if successful, otherwise None.
        """
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {
                    "$set": {
                        "titulo": title,
                        "autor": author,
                        "ano": year,
                        "preco": price,
                    }
                },
            )
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating the book: {e}")
            return None

    def delete_book(self, id: str):
        """
        Deletes a book entry from the database by its ID.

        Args:
            id (str): The ID of the book to delete.

        Returns:
            int or None: The number of documents deleted if successful, otherwise None.
        """
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting the book: {e}")
            return None
