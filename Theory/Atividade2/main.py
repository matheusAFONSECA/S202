import threading
import time
import random
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["bancoiot"]
collection = db["sensores"]

# Function to simulate the sensor
def simulate_sensor(sensor_name):
    """
    Simulates the operation of a temperature sensor in an IoT network.

    This function generates random temperature readings for a specific sensor and stores them
    in a MongoDB database. If the generated temperature exceeds 38°C, the sensor is marked as
    'alarmed' and an alert message is displayed. Once alarmed, the sensor no longer generates 
    temperature readings.

    Args:
        sensor_name (str): The name of the sensor, used as an identifier in MongoDB.

    Returns:
        None
    """

    # Initial sensor document in MongoDB
    sensor_document = {
        "nomeSensor": sensor_name,
        "valorSensor": 0,
        "unidadeMedida": "C°",
        "sensorAlarmado": False,
    }
    # Insert the initial document into MongoDB
    collection.insert_one(sensor_document)

    while True:
        # Fetch the sensor document from MongoDB
        sensor = collection.find_one({"nomeSensor": sensor_name})

        if sensor["sensorAlarmado"]:
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor_name}!")
            break

        # Generate a random temperature value between 30 and 40
        temperature = random.uniform(30, 40)
        print(f"Sensor {sensor_name} - Temperatura: {temperature:.2f} C°")

        # Update the document in MongoDB with the new temperature
        collection.update_one(
            {"nomeSensor": sensor_name}, {"$set": {"valorSensor": temperature}}
        )

        # Check if the temperature is higher than 38°C and update the alarm status
        if temperature > 38:
            collection.update_one(
                {"nomeSensor": sensor_name}, {"$set": {"sensorAlarmado": True}}
            )

        # Wait for 2 seconds before the next reading
        time.sleep(2)


# Main function to create and start threads
if __name__ == "__main__":
    # List of sensors
    sensors = ["Temp1", "Temp2", "Temp3"]
    threads = []

    # Create and start a thread for each sensor
    for sensor in sensors:
        thread = threading.Thread(target=simulate_sensor, args=(sensor,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
