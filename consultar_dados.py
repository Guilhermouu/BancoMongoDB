import pymongo
import pymongo.errors
try:        
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    banco= client["Clientes"]
    collection = banco ["Jogos"]

    results = collection.find()
    
    #jogos= colecao.find_one({"Jogos":nome})

    #results = collection.find({"Jogos": "Forza Horizon"})

    #results = collection.find({"Jogos": 1, "Sistema Operacional": 1})
    result_lista = list(results)
    print("O resultado é: ",result_lista)
except pymongo.erros as e:
    print('Vixe acabou dando erro aí em', e)