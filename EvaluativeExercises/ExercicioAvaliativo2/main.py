from database import Database
from modules.teacherCLI import TeacherCLI
from modules.teacherCRUD import TeacherCRUD

if __name__ == "__main__":
    # Create an instance of the Database class, passing in the connection details for the Neo4j database
    db = Database("bolt://44.203.212.164:7687", "neo4j", "sewers-vine-forms")

    # Create an instance of the TeacherCRUD class, passing in the Database instance
    teacher_crud = TeacherCRUD(db)

    # # Creating a new teacher node
    # teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

    # # Reading the teacher node
    # print(teacher_crud.read("Chris Lima"))

    # # Updating the teacher node
    # teacher_crud.update("Chris Lima", "162.052.777-77")

    # # Reading the teacher node to see if information was updated
    # print(teacher_crud.read("Chris Lima"))

    # Startirg the CLI
    TeacherCLI(teacher_crud).run()

    # Closing the database connection
    db.close()
