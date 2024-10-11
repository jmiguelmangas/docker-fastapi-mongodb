from pymongo import MongoClient

def get_database():
    # Conexión a MongoDB, que corre en localhost en el puerto 27017
    client = MongoClient("mongodb://localhost:27017/")

    return client["mydatabase"]
