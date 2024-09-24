from classes.corrida import Corrida
from classes.motorista import Motorista
from classes.passageiro import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_Dao):
        super().__init__()
        self.motorista_Dao = motorista_Dao
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)
        
    def create(self):
        notafinal = 0
        # Criando um passageiro
        nome = input("Digite o nome do passageiro: ")
        documento = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome, documento)

        corridas = []
        numeroCorridas = int(input("Digite o número de corridas? Maior ou igual a 1: "))
        for i in range(numeroCorridas):    
            nota = float(input("Digite a nota da corrida: "))
            notafinal += nota
            distancia = float(input("Digite a distância percorrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro.dict())
            corridas.append(vars(corrida))
            
        # Criando um motorista e adicionando as corridas realizadas a sua lista
        motorista = Motorista(corridas, notafinal / numeroCorridas)
        # Salvando o motorista no banco de dados
        self.motorista_Dao.create(motorista)
        print("Motorista cadastrado com sucesso.")
        
    def update(self):
        id = str(input("Entre com o id: "))
        motorista = self.motorista_Dao.read(id)
        
        if motorista:
            # Criando um novo passageiro
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)

            novas_corridas = []
            numeroCorridas = int(input("Digite o número de novas corridas: "))
            for i in range(numeroCorridas):    
                nota = float(input("Digite a nota da corrida: "))
                distancia = float(input("Digite a distância percorrida: "))
                valor = float(input("Digite o valor da corrida: "))
                corrida = Corrida(nota, distancia, valor, passageiro.dict())
                novas_corridas.append(vars(corrida))  
                
            # Atualizando as corridas realizadas
            self.motorista_Dao.update(id, novas_corridas)             
            print("Motorista alterado com sucesso.")
        else:
            print("Motorista não encontrado.")

        
    def read(self):
        id = str(input("Entre com o id: "))
        motorista = self.motorista_Dao.read(id)
        # imprimindo as corridas 
        if motorista:
            print(f"Nota Final da soma das Corridas: {motorista['nota']}")
            for motoristas in motorista['corridas']:
                print(f"**************************************")
                print(f"Nota: {motoristas['nota']}")
                print(f"Distancia: {motoristas['distancia']}")
                print(f"Valor: {motoristas['valor']}")
                print(f"Nome passageiro: {motoristas['passageiro']['nome']}")
                print(f"Documento passageiro: {motoristas['passageiro']['documento']}")
        if not motorista:
            print("Não encontrado!!.")
    
    def delete(self):
        id = str(input("Entre com o id: "))
        motorista = self.motorista_Dao.read(id)
        if motorista:
            self.motorista_Dao.delete(id)
            print("Motorista deletado com sucesso.")
        else:
            print("Motorista não encontrado.")
    
    def run(self):
        print("Bem vindo ao Motorista CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()