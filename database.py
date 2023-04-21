from typing import Collection
import pymongo # pip install pymongo



class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://moreirajoaopedro99:senha1@cluster0.vspzhr0.mongodb.net/test"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def disconnect(self):
        try:
            self.db.drop_collection(self.collection)
            print("Banco de dados desconectado com sucesso!")
        except Exception as e:
            print(e)