import pymongo
import pymongo.errors

try:
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        
        banco = client["Clientes"]
        
        collection = banco["Jogos"]
        
        collection.update_one({"author": "Mike"}, {"$set": {"text": "Hello,MongoDB!"}})

        collection.update_one({"author": "Tom"}, {"$inc": {"views": 1}})
except pymongo.erros as e:
    print('Deu erro aí nesse bagui ai vey')