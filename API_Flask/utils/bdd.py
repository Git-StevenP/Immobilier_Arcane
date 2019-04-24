from pymongo import MongoClient

class MongoDB():
    
    def __init__(self,dbname):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[dbname]

    def get_collection_name(self):
        #Return all collection names
        return self.db.collection_names()

    def find(self, collection, what=dict(), _id=False, last=False):
        #by default the function doesn't select the _id field
        #retourne une list de dictionaire last=False
        #retourne un dictionaire si last=True
        if _id == False:
            cursor = self.db[collection].find(what, {'_id': False})
        else:
            cursor = self.db[collection].find(what)

        if last == True:
            cursor = cursor.sort([("Time", -1)]).limit(1)
            return cursor[0]
        return self.cursor_to_dict(cursor)

    def find_all_last(self, what=dict(), _id=False, last=False):
        d = dict()
        for coll in self.get_collection_name():
            if coll == "users":
                continue
            d[coll] = self.find(coll, what, _id, last)
        return d

    def insert_one(self, collection, item):
        try:
            #Insertion de l'item dans la base de donnees
            self.db[collection].insert_one(item)
            return 1
        except:
            print("Item non importe")
            return -1

    def cursor_to_dict(self, cursor):
        l = list()
        for i in cursor:
            l.append(i)
        return l

    def get_keys(self, collection):
        #Return all field name of a collection
        map = Code("function() { for (var key in this) { emit(key, null); } }")
        reduce = Code("function(key, stuff) { return null; }")
        result = self.db[collection].map_reduce(map, reduce, "myresults")
        return result.distinct('_id')

    def update_real_estate(self, real_estate_name, attr_key, attr_to_update):
        """Met à jour la base de données en fonction du nom du bien immobilier, et de l'attribut qu'il faut modifier.

        Paramètres nommés :
        self -- le base de données elle-même
        real_estate_name -- le nom du bien immobilier
        attr_key -- la clé associé à l'attribut devant être modifié
        attr_to_update -- l'attribut devant être modifié
        """

        real_estate_collection = self.db.biens_immobilier 
        real_estate_collection.update({'name' : real_estate_name}, {'$set' : {attr_key :  attr_to_update}})
