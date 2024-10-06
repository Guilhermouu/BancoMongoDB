
import pymongo
import pymongo.errors    
def deletar_um():
      
            client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
            print('Banco de dados conectado com sucesso')

            banco= client["Jogos"]
    
            collection= banco["JogosparaVenda"]

            nome_deletar=input('Informe o que você deseja deletar:')
            
            try:
                resultado= collection.delete_one({"Jogos": nome_deletar})
                if resultado:
                    print(f"Jogo '{nome_deletar}' deletado com sucesso.")
                else:
                    print(f"Nenhum dado foi deletado para '{nome_deletar}'.")
            except pymongo.errors.PyMongoError as e:
                print("Erro ao deletar jogo:", e)


