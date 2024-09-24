from database import Database
from utils.motoristaDAO import MotoristaDAO
from utils.motoristaCLI import MotoristaCLI

db = Database(database="atividade1", collection="motoristas")
motoristaDao = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDao)
motoristaCLI.run()