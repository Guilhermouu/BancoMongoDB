import pymongo
import pymongo.errors
def inserir_dados():
 try:
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        banco = client["Jogos"]
        collection = banco["JogosparaVenda"]

        jogo_nome = input("Digite o nome do jogo: ")

        preco = input("Digite o preço do jogo: ")

        sistemas = input("Digite os sistemas operacionais suportados separados por vírgula: ")

        sistemas_list = [sistema.strip() for sistema in sistemas.split(",")]

        post = {
        "Jogos": jogo_nome,
        "Preço": preco,
        "Sistemas Operacionais Suportaveis": sistemas_list
         }


        post_id = collection.insert_one(post).inserted_id

 except pymongo.errors as e:
        print('Vixe foi erro aqui tbm',e)
