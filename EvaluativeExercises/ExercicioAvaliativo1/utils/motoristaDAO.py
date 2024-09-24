from bson.objectid import ObjectId
from classes.motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database
    
    def create(self, motorista: Motorista):
        try:
            res = self.db.collection.insert_one(vars(motorista))
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista found")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update(self, id: str, novas_corridas: list):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(id)})
            if motorista:
                # Atualizando as corridas
                motorista['corridas'].extend(novas_corridas)

                # Recalculando a média das notas
                notas = [corrida['nota'] for corrida in motorista['corridas']]
                motorista['nota'] = sum(notas) / len(notas)

                # Atualizando o documento no MongoDB
                res = self.db.collection.update_one(
                    {"_id": ObjectId(id)},
                    {'$set': motorista}
                )
                print(f"Motorista updated: {res.modified_count} document(s) modified")
                return res.modified_count
            else:
                print("Motorista não encontrado.")
                return None
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None