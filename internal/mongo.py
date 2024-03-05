from bson.json_util import dumps
from pymongo import MongoClient
from configparser import ConfigParser

class Mongo:

    def __init__(self, filename):
        config = ConfigParser()
        config.read(filename)

        host = config['mongo']['mongo_host']
        port = int(config['mongo']['mongo_port'])
        user = config['mongo']['mongo_user']
        password = config['mongo']['mongo_pass']
        dbname = config['mongo']['mongo_name']

        #self.conn = MongoClient(f'mongodb://{user}:{password}@{host}:{port}', authSource=dbname, authMechanism='SCRAM-SHA-256')
        self.conn = MongoClient(host=host, port=port, username=user, password=password, authSource=dbname, authMechanism='SCRAM-SHA-256')
        self.db = self.conn[dbname]
        self.coll = self.db[config['mongo']['mongo_coll']]
    
    @property
    def collection(self):
        return self.coll

    def __exit__(self):
        self.conn.close()

def pprint(element):
    print(dumps(element, indent=2))
