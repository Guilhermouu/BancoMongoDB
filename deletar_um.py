# Importa a biblioteca pymongo para interagir com o MongoDB
import pymongo
# Importa a sub-biblioteca de erros do pymongo para tratamento de exceções
import pymongo.errors    

# Define uma função para deletar um jogo do banco de dados
def deletar_um():
    # Cria um cliente MongoDB usando a string de conexão
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    # Imprime uma mensagem de sucesso ao conectar ao banco de dados
    print('Banco de dados conectado com sucesso')

    # Seleciona o banco de dados chamado "Jogos"
    banco = client["Jogos"]
    # Seleciona a coleção chamada "JogosparaVenda" dentro do banco de dados
    collection = banco["JogosparaVenda"]

    # Solicita ao usuário o nome do jogo que deseja deletar
    nome_deletar = input('Informe o que você deseja deletar:')

    try:
        # Tenta deletar um documento na coleção onde o campo "Jogos" é igual ao nome_deletar
        resultado = collection.delete_one({"Jogos": nome_deletar})
        
        # Verifica se o documento foi deletado e imprime uma mensagem apropriada
        if resultado.deleted_count > 0:
            print(f"Jogo '{nome_deletar}' deletado com sucesso.")
        else:
            print(f"Nenhum dado foi deletado para '{nome_deletar}'.")

    # Captura exceções específicas do pymongo durante a deleção
    except pymongo.errors.PyMongoError as e:
        # Imprime uma mensagem de erro caso a deleção falhe
        print("Erro ao deletar jogo:", e)
