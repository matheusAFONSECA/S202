from database import Database
from bookModel import BookModel
from cli import BookCLI

# Initializes the Database instance.
db = Database(database="relatorio_05", collection="livros")

# Initializes the BookModel instance with the Database instance.
bookModel = BookModel(database=db)

# Initializes the BookCLI instance with the BookModel instance.
bookCLI = BookCLI(bookModel)

# Starts the CLI loop, allowing the user to execute book management commands.
bookCLI.run()
