class GamesManager:
    """
    A class to manage players and matches in a database.

    This class allows for the creation, update, deletion, and retrieval of both players and matches. It interacts with a Neo4j-like database for storing and querying game data.

    Attributes:
        db (Database): An instance of the database to execute queries.
    """

    def __init__(self, database):
        """
        Initializes the GamesManager with a database instance.

        Args:
            database (Database): The database instance used to execute queries.
        """
        self.db = database

    # Create a player
    def create_player(self, player_id, name):
        """
        Creates a new player in the database.

        Args:
            player_id (int): The unique ID of the player.
            name (str): The name of the player.
        """
        query = "CREATE (:Player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    # Update player name
    def update_player(self, player_id, new_name):
        """
        Updates the name of an existing player in the database.

        Args:
            player_id (int): The unique ID of the player.
            new_name (str): The new name for the player.
        """
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    # Delete player
    def delete_player(self, player_id):
        """
        Deletes a player from the database.

        Args:
            player_id (int): The unique ID of the player to delete.
        """
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    # Retrieve list of players
    def get_players(self):
        """
        Retrieves all players from the database.

        Returns:
            list: A list of dictionaries containing player IDs and names.
        """
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    # Create a match
    def create_match(self, match_id, player1_id, player2_id, result):
        """
        Creates a new match between two players in the database.

        Args:
            match_id (int): The unique ID of the match.
            player1_id (int): The unique ID of player 1.
            player2_id (int): The unique ID of player 2.
            result (str): The result of the match.
        """
        query = """
        MATCH (p1:Player {id: $player1_id}), (p2:Player {id: $player2_id})
        CREATE (m:Match {id: $match_id, result: $result})
        CREATE (p1)-[:PARTICIPATED_IN]->(m)
        CREATE (p2)-[:PARTICIPATED_IN]->(m)
        """
        parameters = {
            "match_id": match_id,
            "player1_id": player1_id,
            "player2_id": player2_id,
            "result": result,
        }
        self.db.execute_query(query, parameters)

    # Update match result
    def update_match_result(self, match_id, new_result):
        """
        Updates the result of an existing match in the database.

        Args:
            match_id (int): The unique ID of the match.
            new_result (str): The new result for the match.
        """
        query = "MATCH (m:Match {id: $match_id}) SET m.result = $new_result"
        parameters = {"match_id": match_id, "new_result": new_result}
        self.db.execute_query(query, parameters)

    # Delete match
    def delete_match(self, match_id):
        """
        Deletes a match from the database.

        Args:
            match_id (int): The unique ID of the match to delete.
        """
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    # Retrieve specific match
    def get_match(self, match_id):
        """
        Retrieves a specific match and the players who participated in it.

        Args:
            match_id (int): The unique ID of the match.

        Returns:
            dict or None: A dictionary containing the match ID, result, and players' names if found, otherwise None.
        """
        query = """
        MATCH (m:Match {id: $match_id})<-[:PARTICIPATED_IN]-(p:Player)
        RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players
        """
        parameters = {"match_id": match_id}
        result = self.db.execute_query(query, parameters)
        if result:
            return {
                "match_id": result[0]["match_id"],
                "result": result[0]["result"],
                "players": result[0]["players"],
            }
        else:
            return None

    # Player's match history
    def get_player_history(self, player_id):
        """
        Retrieves the match history of a specific player.

        Args:
            player_id (int): The unique ID of the player.

        Returns:
            list: A list of dictionaries containing match IDs and results.
        """
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m.id AS match_id, m.result AS result
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [
            {"match_id": result["match_id"], "result": result["result"]}
            for result in results
        ]
