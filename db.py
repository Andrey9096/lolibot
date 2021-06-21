
from pymongo import MongoClient

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class DB_CONNECT(object):
    client = MongoClient('127.0.0.1', 27017)
    db = client["Admins"]
    dblist = client.list_database_names()

    if "Admins" in dblist:
        print("База уже существует")