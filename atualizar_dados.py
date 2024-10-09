# Importa a função conectar_banco do módulo banco_dados
from banco_dados import conectar_banco
# Importa a biblioteca pymongo para interagir com o MongoDB
import pymongo

# Define uma função para atualizar os dados de um jogo
def atualizar_jogo():
    # Chama a função conectar_banco() para obter a coleção de jogos
    collection = conectar_banco()
 
    # Solicita ao usuário o nome do jogo que deseja atualizar
    nome_jogo = input('Informe o novo jogo que deseja atualizar: ')
     
    # Pergunta ao usuário quais dados ele deseja alterar (Jogos, Preço, Sistemas Operacionais Suportaveis)
    alterar = input('Quais dados você desejaria alterar Jogos, Preço, Sistemas Operacionais Suportaveis? ')

    # Solicita os novos dados que serão atualizados
    novos_dados = input("Informe os novos dados a serem atualizados: ")

    try:
        # Atualiza um documento na coleção onde o campo "Jogos" é igual ao nome_jogo,
        # definindo o novo valor para o campo especificado em alterar
        resultado = collection.update_one({"Jogos": nome_jogo}, {"$set": {alterar: novos_dados}})

        # Verifica se algum documento foi atualizado e imprime uma mensagem apropriada
        if resultado.modified_count > 0:
            print(f"Jogo '{nome_jogo}' atualizado com sucesso.")
        else:
            print(f"Nenhuma atualização foi feita para '{nome_jogo}'.")

    # Captura exceções específicas do pymongo durante a atualização
    except pymongo.errors.PyMongoError as e:
        # Imprime uma mensagem de erro caso a atualização falhe
        print("Erro ao atualizar jogo:", e)
