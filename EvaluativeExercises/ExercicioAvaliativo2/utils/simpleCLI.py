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