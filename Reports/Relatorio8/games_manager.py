class GamesManager:
    def __init__(self, database):
        self.db = database

    # Criar jogador
    def create_player(self, player_id, name):
        query = "CREATE (:Player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    # Atualizar nome do jogador
    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    # Deletar jogador
    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    # Recuperar lista de jogadores
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    # Criar partida
    def create_match(self, match_id, player1_id, player2_id, result):
        query = """
        MATCH (p1:Player {id: $player1_id}), (p2:Player {id: $player2_id})
        CREATE (m:Match {id: $match_id, result: $result})
        CREATE (p1)-[:PARTICIPATED_IN]->(m)
        CREATE (p2)-[:PARTICIPATED_IN]->(m)
        """
        parameters = {"match_id": match_id, "player1_id": player1_id, "player2_id": player2_id, "result": result}
        self.db.execute_query(query, parameters)

    # Atualizar resultado da partida
    def update_match_result(self, match_id, new_result):
        query = "MATCH (m:Match {id: $match_id}) SET m.result = $new_result"
        parameters = {"match_id": match_id, "new_result": new_result}
        self.db.execute_query(query, parameters)

    # Deletar partida
    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    # Recuperar uma partida específica
    def get_match(self, match_id):
        query = """
        MATCH (m:Match {id: $match_id})<-[:PARTICIPATED_IN]-(p:Player)
        RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players
        """
        parameters = {"match_id": match_id}
        result = self.db.execute_query(query, parameters)
        if result:
            return {"match_id": result[0]["match_id"], "result": result[0]["result"], "players": result[0]["players"]}
        else:
            return None

    # Histórico de partidas de um jogador
    def get_player_history(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m.id AS match_id, m.result AS result
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"match_id": result["match_id"], "result": result["result"]} for result in results]

