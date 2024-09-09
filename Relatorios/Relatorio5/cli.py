class SimpleCLI:
    """
    A basic Command Line Interface (CLI) for executing commands.

    Attributes:
        commands (dict): A dictionary that maps command names to their corresponding functions.
    """

    def __init__(self):
        """
        Initializes the SimpleCLI with an empty command dictionary.
        """
        self.commands = {}

    def add_command(self, name, function):
        """
        Adds a new command to the CLI.

        Args:
            name (str): The name of the command.
            function (callable): The function to be executed when the command is entered.
        """
        self.commands[name] = function

    def run(self):
        """
        Starts the CLI loop, allowing users to input commands and execute associated functions.
        The loop continues until the user enters 'quit'.
        """
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class BookCLI(SimpleCLI):
    """
    A CLI for managing books with CRUD operations.

    Inherits from:
        SimpleCLI: Provides basic CLI functionality and command execution.

    Attributes:
        book_model (object): An instance of a book model that handles CRUD operations.
    """

    def __init__(self, book_model):
        """
        Initializes the BookCLI with the given book model and adds book management commands.

        Args:
            book_model (object): An instance of the book model to interact with.
        """
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)
        self.add_command("quit", self.quit)

    def create_book(self):
        """
        Prompts the user for book details and creates a new book using the book model.
        """
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        price = float(input("Enter the price: "))
        self.book_model.create_book(title, author, year, price)

    def read_book(self):
        """
        Prompts the user for a book ID and displays the details of the book with that ID.
        """
        id = input("Enter the id: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Title: {book['titulo']}")
            print(f"Author: {book['autor']}")
            print(f"Year: {book['ano']}")
            print(f"Price: {book['preco']}")

    def update_book(self):
        """
        Prompts the user for a book ID and new details, and updates the book with the given ID.
        """
        id = input("Enter the id: ")
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        year = int(input("Enter the new year: "))
        price = float(input("Enter the new price: "))
        self.book_model.update_book(id, title, author, year, price)

    def delete_book(self):
        """
        Prompts the user for a book ID and deletes the book with that ID.
        """
        id = input("Enter the id: ")
        self.book_model.delete_book(id)

    def quit(self):
        """
        Exits the Book CLI.
        """
        print("Exiting the Book CLI.")
        exit()

    def run(self):
        """
        Starts the BookCLI loop, displaying a welcome message and the available commands.
        """
        print("Welcome to the book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
