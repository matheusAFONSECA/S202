from database import Database
from pokedex import Pokedex

# load the database
db = Database(database="pokedex", collection="pokemons")

# create the database and insert the dataset
# db.resetDatabase()

# creating a pokedex object
pokedex = Pokedex(database=db)

pokedex.get_pokemons_weak_against_water()
pokedex.get_pokemons_type_poisson()
pokedex.get_pokemons_without_evolution()
pokedex.get_pokemons_two_weakness()
pokedex.get_pokemons_avg_spawns_less_five()
