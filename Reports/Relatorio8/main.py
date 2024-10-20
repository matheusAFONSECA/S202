from database import Database
from games_manager import GamesManager

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.204.57.22:7687", "neo4j", "sales-nurse-acquittals")
db.drop_all()

# Criando o gerenciador de jogos
game_manager = GamesManager(db)

# Criando os jogadores
game_manager.create_player("1", "Alvaro")
game_manager.create_player("2", "Gabriel Siqueria")
game_manager.create_player("3", "Ewel")

# Adicionando o jogador Chico e atualizando o nome para Xico
game_manager.create_player("4", "Chico")
game_manager.update_player("4", "Xico")

# Deletando o jogador Ewel
game_manager.delete_player("3")

# Criando algumas partidas
game_manager.create_match("m1", "1", "2", "1")  # Alvaro venceu Gabriel Siqueria
game_manager.create_match("m2", "1", "4", "4")  # Xico venceu Alvaro

# Recuperando a lista de jogadores
print("Jogadores:")
for player in game_manager.get_players():
    print(f"ID: {player['id']}, Nome: {player['name']}")

db.close()