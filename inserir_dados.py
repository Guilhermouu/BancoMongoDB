import pymongo
import pymongo.errors
#def inserir_dados():
try:
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        banco = client["Clientes"]
        collection = banco["Jogos"]
        
        post = {"'Jogos'":  "Gta 5", "Sistema Operacional": ["Windows","Linux", "PS4"]}
            
        post_id = collection.insert_one(post).inserted_id
except pymongo.errors as e:
        print('Vixe foi erro aqui tbm',e)
#inserir_dados()