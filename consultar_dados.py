# Importa a biblioteca pymongo para interagir com o MongoDB
import pymongo
# Importa a sub-biblioteca de erros do pymongo para tratamento de exceções
import pymongo.errors

# Define uma função para consultar todos os dados no banco de dados
def consultar_todos_dados():
    try:
        # Cria um cliente MongoDB usando a string de conexão
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        # Seleciona o banco de dados chamado "Jogos"
        banco = client["Jogos"]
        # Seleciona a coleção chamada "JogosparaVenda" dentro do banco de dados
        collection = banco["JogosparaVenda"]
        
        # Busca todos os documentos na coleção
        resultados = collection.find()

        # Converte o cursor de resultados em uma lista
        resultado_lista = list(resultados)

        # Imprime a lista de resultados encontrados
        print("O resultado é: ", resultado_lista)

    # Captura exceções específicas do pymongo durante a consulta
    except pymongo.errors as e:
        # Imprime uma mensagem de erro caso a consulta falhe
        print('Vixe acabou dando erro aí em', e)
