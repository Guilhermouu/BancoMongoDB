# Importa a biblioteca pymongo, que permite interagir com o MongoDB
import pymongo
# Importa a sub-biblioteca de erros do pymongo, que é utilizada para tratamento de exceções
import pymongo.errors

# Define uma função para conectar ao banco de dados
def conectar_banco():
    try:
        # Cria um cliente MongoDB usando a string de conexão
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        # Imprime uma mensagem de sucesso ao conectar ao banco de dados
        print('Banco de dados conectado com sucesso')

        # Seleciona o banco de dados chamado "Jogos"
        banco = client["Jogos"]
    
        # Seleciona a coleção chamada "JogosparaVenda" dentro do banco de dados
        collection = banco["JogosparaVenda"]

        # Retorna a coleção selecionada para uso posterior
        return collection
       
    # Captura exceções específicas do pymongo durante a conexão
    except pymongo.errors as e:
        # Imprime uma mensagem de erro caso a conexão falhe
        print("Foi um Erro aí e deu ruim", e)
