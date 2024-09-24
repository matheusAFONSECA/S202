from classes.corrida import Corrida
from classes.motorista import Motorista
from classes.passageiro import Passageiro


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


class MotoristaCLI(SimpleCLI):
    """
    Command Line Interface (CLI) for managing 'Motorista' entities.
    This class provides a simple CLI to create, read, update, and delete
    'Motorista' entities using a provided DAO (Data Access Object).
    Methods
    -------
    __init__(motorista_Dao)
        Initializes the CLI with the provided DAO and sets up commands.
    create()
        Prompts the user to input details for creating a new 'Motorista' and saves it using the DAO.
    update()
        Prompts the user to input details for updating an existing 'Motorista' and updates it using the DAO.
    read()
        Prompts the user to input an ID and retrieves the corresponding 'Motorista' details from the DAO.
    delete()
        Prompts the user to input an ID and deletes the corresponding 'Motorista' from the DAO.
    run()
        Starts the CLI and displays available commands.
    """

    def __init__(self, motorista_Dao):
        """
        Initialize the MotoristaCLI class.

        Args:
            motorista_Dao (object): An instance of the MotoristaDAO class used for data access operations.

        This constructor initializes the MotoristaCLI class by setting up the data access object and
        adding the CRUD commands (create, read, update, delete) to the command list.
        """
        super().__init__()
        self.motorista_Dao = motorista_Dao
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)

    def create(self):
        """
        Creates a new driver with associated rides and saves it to the database.
        This method prompts the user to input details for a passenger and multiple rides.
        It then calculates the average rating of the rides and creates a driver instance
        with these rides and the calculated average rating. Finally, it saves the driver
        instance to the database.
        Inputs:
            - Passenger name (str): The name of the passenger.
            - Passenger document (str): The document identifier of the passenger.
            - Number of rides (int): The number of rides to be added (must be >= 1).
            - Ride rating (float): The rating for each ride.
            - Ride distance (float): The distance covered in each ride.
            - Ride value (float): The monetary value of each ride.
        Side effects:
            - Prompts the user for input.
            - Prints a success message upon completion.
        Raises:
            ValueError: If the number of rides is less than 1.
        """
        notafinal = 0
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

        motorista = Motorista(corridas, notafinal / numeroCorridas)
        self.motorista_Dao.create(motorista)
        print("Motorista cadastrado com sucesso.")

    def update(self):
        """
        Updates the information of a motorista (driver) in the system.
        Prompts the user to enter the ID of the motorista to update. If the motorista
        is found, it allows the user to input new information for the motorista's
        passageiro (passenger) and the details of new corridas (rides). The updated
        information is then saved in the motorista_Dao.
        Parameters:
        None
        Returns:
        None
        Prompts:
        - ID of the motorista
        - Name of the passageiro
        - Document of the passageiro
        - Number of new corridas
        - For each corrida:
            - Note of the corrida
            - Distance of the corrida
            - Value of the corrida
        Prints:
        - Success message if the motorista is updated
        - Error message if the motorista is not found
        """
        id = str(input("Entre com o id: "))
        motorista = self.motorista_Dao.read(id)

        if motorista:
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

            self.motorista_Dao.update(id, novas_corridas)
            print("Motorista alterado com sucesso.")
        else:
            print("Motorista não encontrado...")

    def read(self):
        id = str(input("Entre com o id: "))
        motorista = self.motorista_Dao.read(id)
        # imprimindo as corridas
        if motorista:
            print(f"Nota Final da soma das Corridas: {motorista['nota']}")
            for motoristas in motorista["corridas"]:
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Nota: {motoristas['nota']}")
                print(f"Distancia: {motoristas['distancia']}")
                print(f"Valor: {motoristas['valor']}")
                print(f"Nome passageiro: {motoristas['passageiro']['nome']}")
                print(f"Documento passageiro: {motoristas['passageiro']['documento']}")
        if not motorista:
            print("Não encontrado...")

    def delete(self):
        """
        Deletes a motorista (driver) record based on the provided ID.

        Prompts the user to enter an ID, then attempts to read the motorista
        record from the database. If the record exists, it deletes the motorista
        and prints a success message. If the record does not exist, it prints
        an error message.

        Returns:
            None
        """
        id = str(input("Entre com o id: "))
        motorista = self.motorista_Dao.read(id)
        if motorista:
            self.motorista_Dao.delete(id)
            print("Motorista deletado com sucesso.")
        else:
            print("Motorista não encontrado...")

    def run(self):
        """
        Executes the command-line interface (CLI) for the motorista application.

        This method prints a welcome message and a list of available commands
        (create, read, update, delete, quit) to the console. It then calls the
        `run` method of the superclass to continue execution.

        Returns:
            None
        """
        print("Bem vindo ao CLI da Colleation motorista!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()
