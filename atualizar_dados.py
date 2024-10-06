from banco_dados import conectar_banco
import pymongo
def atualizar_jogo():
    collection = conectar_banco()
 
    nome_jogo=input('Informe o novo jogo que deseja atualizar: ')
     
    alterar= input('Que dado você desejaria alterar? Jogos, Preço, Sistemas Operacionais Suportaveis ')

    novos_dados=input("Informe os novos dados a serem atualizados: ")


    try:
     
        resultado = collection.update_one({"Jogos": nome_jogo}, {"$set" : {alterar:novos_dados}})

        if resultado:
            print(f"Jogo '{nome_jogo}' atualizado com sucesso.")
        else:
            print(f"Nenhuma atualização foi feita para '{nome_jogo}'.")

    except pymongo.errors.PyMongoError as e:
        print("Erro ao atualizar jogo:", e)

