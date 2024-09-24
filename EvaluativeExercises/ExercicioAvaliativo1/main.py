from database import Database
from utils.motoristaDAO import MotoristaDAO
from utils.motoristaCLI import MotoristaCLI

"""
This script initializes the database connection and runs the MotoristaCLI.
Modules:
    database: Contains the Database class for database operations.
    utils.motoristaDAO: Contains the MotoristaDAO class for data access operations.
    utils.motoristaCLI: Contains the MotoristaCLI class for command-line interface operations.
Classes:
    Database: Manages the connection to the database.
    MotoristaDAO: Handles data access operations for the 'motoristas' collection.
    MotoristaCLI: Provides a command-line interface for interacting with motorista data.
Usage:
    Run this script to start the MotoristaCLI, which allows interaction with the motorista data.
"""
db = Database(database="atividade1", collection="motoristas")
motoristaDao = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDao)
motoristaCLI.run()
