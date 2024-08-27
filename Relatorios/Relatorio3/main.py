from database import Database
from helper.writeAJson import writeAJson

# load the database
db = Database(database="pokedex", collection="pokemons")

# db.resetDatabase()    # create the database and insert the dataset