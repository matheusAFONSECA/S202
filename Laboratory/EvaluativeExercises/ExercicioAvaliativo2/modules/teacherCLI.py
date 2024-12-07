from utils.simpleCLI import SimpleCLI


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        """
        Initialize the TeacherCLI with CRUD operations.

        Args:
            teacher_crud (TeacherCRUD): An instance of the TeacherCRUD class to handle
                                        create, read, update, and delete operations.

        Attributes:
            teacher_crud (TeacherCRUD): Stores the instance of TeacherCRUD.
        """
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        """
        Prompts the user to input the details of a new teacher and creates a teacher record.

        The method will ask for the teacher's name, birth year, and CPF (Cadastro de Pessoas Físicas).
        It then uses the teacher_crud object to create a new teacher record with the provided details.

        Inputs:
            - Name: str, the name of the teacher.
            - Birth year: int, the birth year of the teacher.
            - CPF: str, the CPF (Cadastro de Pessoas Físicas) of the teacher.
        Side effects:
            - Prints messages to the console.
            - Reads input from the user.
            - Calls the create method on the teacher_crud object to create a new teacher record.
        """
        print("Creating a new teacher")
        name = input("Name: ")
        ano_nasc = int(input("Birth year: "))
        cpf = input("CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        """
        Prompts the user to enter a teacher's name, retrieves the teacher's information
        from the teacher_crud, and prints the teacher's details.

        Inputs:
            - Prompts the user to input the teacher's name.

        Side Effects:
            - Reads input from the user.
            - Prints the teacher's information to the console.
        """
        name = input("Enter the teacher's name: ")
        teacher = self.teacher_crud.read(name)
        print(teacher)

    def update_teacher(self):
        """
        Updates a teacher's information by prompting the user for the teacher's name and new CPF.

        Inputs:
            - Prompts the user to input the teacher's name.
            - Prompts the user to input the teacher's new CPF.

        Side effects:
            - Prints messages to the console.
            - Calls the `update` method of `self.teacher_crud` with the provided name and new CPF.
        """
        print("Updating a teacher's information")
        name = input("Name: ")
        new_cpf = input("CPF: ")
        self.teacher_crud.update(name, new_cpf)

    def delete_teacher(self):
        """
        Prompts the user to enter the name of a teacher and deletes the teacher
        from the system.

        Inputs:
            - Prompts the user to enter the teacher's name via the standard input.

        Side Effects:
            - Calls the delete method of the teacher_crud attribute with the entered
            teacher's name, which removes the teacher from the system.
            - Interacts with the user through the console.
        """
        name = input("Enter the teacher's name: ")
        self.teacher_crud.delete(name)

    def run(self):
        """
        Executes the command-line interface (CLI) for the teacher database.

        This method prints a welcome message and a list of available commands
        (create, read, update, delete, quit) to the console. It then calls the
        `run` method of the superclass to continue execution.
        """
        print("Welcome to a CLI for teacher database!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
