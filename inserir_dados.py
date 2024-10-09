
import pymongo
import pymongo.errors

# Define uma função para inserir dados no banco de dados
def inserir_dados():
    try:
        # Cria um cliente MongoDB usando a string de conexão
        client = pymongo.MongoClient(
            "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        
        # Seleciona o banco de dados chamado "Jogos"
        banco = client["Jogos"]
        
        # Seleciona a coleção chamada "JogosparaVenda" dentro do banco de dados
        collection = banco["JogosparaVenda"]

        # Solicita ao usuário o nome do jogo
        jogo_nome = input("Digite o nome do jogo: ")

        # Solicita ao usuário o preço do jogo
        preco = input("Digite o preço do jogo: ")

        # Solicita ao usuário os sistemas operacionais suportados, separados por vírgula
        sistemas = input(
            "Digite os sistemas operacionais suportados separados por vírgula: ")

        # Divide a string de sistemas em uma lista e remove espaços em branco
        sistemas_list = [sistema.strip() for sistema in sistemas.split(",")]

        # Cria um dicionário com os dados do jogo a serem inseridos
        post = {
            "Jogos": jogo_nome,
            "Preço": preco,
            "Sistemas Operacionais Suportaveis": sistemas_list
        }

        # Insere o dicionário na coleção e captura o ID do documento inserido
        post_id = collection.insert_one(post).inserted_id

    # Captura exceções específicas do pymongo durante a inserção
    except pymongo.errors as e:
        
        # Imprime uma mensagem de erro caso a inserção falhe
        print('Erro ao inserir dados ', e)
