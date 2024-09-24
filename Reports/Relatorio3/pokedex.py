from database import Database
from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, database: Database):
        # Initialize the Pokedex with a database instance
        self._database = database

    def get_pokemons_weak_against_water(self):
        # Retrieve the database instance
        data = self._database
        # Find all pokemons with weakness against Water
        pokemons = data.collection.find({"weaknesses": "Water"})

        # Write the pokemons data to a JSON file
        writeAJson(pokemons, "pokemons_weak_against_water")

    def get_pokemons_type_poisson(self):
        # Retrieve the database instance
        data = self._database
        # Find all pokemons with type Poison
        pokemons = data.collection.find({"type": "Poison"})

        # Write the pokemons data to a JSON file
        writeAJson(pokemons, "pokemons_type_poisson")

    def get_pokemons_without_evolution(self):
        # Retrieve the database instance
        data = self._database
        # Find all pokemons without next evolution
        pokemons = data.collection.find({"next_evolution": {"$exists": False}})

        # Write the pokemons data to a JSON file
        writeAJson(pokemons, "pokemons_without_evolution")

    def get_pokemons_two_weakness(self):
        # Retrieve the database instance
        data = self._database
        # Find all pokemons with two weaknesses
        pokemons = data.collection.find({"weaknesses": {"$size": 2}})

        # Write the pokemons data to a JSON file
        writeAJson(pokemons, "pokemons_with_two_weakness")

    def get_pokemons_avg_spawns_less_five(self):
        # Retrieve the database instance
        data = self._database
        # Find all pokemons with average spawns less than 5
        pokemons = data.collection.find({"avg_spawns": {"$lt": 5}})

        # Write the pokemons data to a JSON file
        writeAJson(pokemons, "pokemons_avg_spawns_less_five")
