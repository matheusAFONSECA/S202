from database import Database
from games_manager import GamesManager

# Create an instance of the Database class, passing in the connection details for the Neo4j database
db = Database("bolt://44.204.57.22:7687", "neo4j", "sales-nurse-acquittals")

# Drop all existing data in the database to start with a clean state
db.drop_all()

# Creating an instance of the GamesManager class
game_manager = GamesManager(db)

# Creating players in the database
game_manager.create_player("1", "Alvaro")  # Creates player Alvaro with ID 1
game_manager.create_player(
    "2", "Gabriel Siqueria"
)  # Creates player Gabriel Siqueria with ID 2
game_manager.create_player("3", "Ewel")  # Creates player Ewel with ID 3

# Adding player Chico and then updating his name to Xico
game_manager.create_player("4", "Chico")  # Creates player Chico with ID 4
game_manager.update_player("4", "Xico")  # Updates the name of player Chico to Xico

# Deleting player Ewel from the database
game_manager.delete_player("3")  # Deletes player Ewel by ID

# Creating some matches between players
game_manager.create_match(
    "m1", "1", "2", "1"
)  # Alvaro won against Gabriel Siqueria in match m1
game_manager.create_match("m2", "1", "4", "4")  # Xico won against Alvaro in match m2

# Retrieving and printing the list of all players from the database
print("Jogadores:")
for player in game_manager.get_players():
    print(
        f"ID: {player['id']}, Nome: {player['name']}"
    )  # Outputs each player's ID and name

# Closing the database connection
db.close()
