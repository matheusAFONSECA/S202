import threading
import time
import random
from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bancoiot"]
collection = db["sensores"]


# Função para simular o sensor
def simular_sensor(nome_sensor):
    """
    Simula o funcionamento de um sensor de temperatura em uma rede IoT.

    Esta função gera leituras de temperatura aleatórias para um sensor específico e as armazena
    em um banco de dados MongoDB. Se a temperatura gerada for superior a 38°C, o sensor é marcado 
    como 'alarmado' e uma mensagem de alerta é exibida. Uma vez alarmado, o sensor não gera mais 
    leituras de temperatura.

    Args:
        nome_sensor (str): O nome do sensor, usado como identificador no MongoDB.

    Retorna:
        None
    """

    # Documento inicial do sensor no MongoDB
    sensor_document = {
        "nomeSensor": nome_sensor,
        "valorSensor": 0,
        "unidadeMedida": "C°",
        "sensorAlarmado": False,
    }
    # Inserir o documento inicial no MongoDB
    collection.insert_one(sensor_document)

    while True:
        # Buscar o documento do sensor no MongoDB
        sensor = collection.find_one({"nomeSensor": nome_sensor})

        if sensor["sensorAlarmado"]:
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!")
            break

        # Gerar um valor de temperatura aleatório entre 30 e 40
        temperatura = random.uniform(30, 40)
        print(f"Sensor {nome_sensor} - Temperatura: {temperatura:.2f} C°")

        # Atualizar o documento no MongoDB com a nova temperatura
        collection.update_one(
            {"nomeSensor": nome_sensor}, {"$set": {"valorSensor": temperatura}}
        )

        # Verificar se a temperatura é superior a 38 C° e atualizar o status de alarmado
        if temperatura > 38:
            collection.update_one(
                {"nomeSensor": nome_sensor}, {"$set": {"sensorAlarmado": True}}
            )

        # Espera de 2 segundos antes da próxima leitura
        time.sleep(2)


# Função principal para criar e iniciar threads
if __name__ == "__main__":
    # Lista de sensores
    sensores = ["Temp1", "Temp2", "Temp3"]
    threads = []

    # Criar e iniciar uma thread para cada sensor
    for sensor in sensores:
        thread = threading.Thread(target=simular_sensor, args=(sensor,))
        thread.start()
        threads.append(thread)

    # Aguardar que todas as threads sejam finalizadas
    for thread in threads:
        thread.join()
