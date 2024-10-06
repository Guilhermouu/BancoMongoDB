import pymongo
import pymongo.errors
def conectar_banco():
    try:
            
            client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
            print('Banco de dados conectado com sucesso')

            banco= client["Jogos"]
    
            collection= banco["JogosparaVenda"]

            return collection
           
    except pymongo.errors as e:
            print("Foi um Erro aí e deu ruim",e)
