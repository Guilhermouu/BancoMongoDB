global opcao
import consultar_dados

def menuconsultar():
    opcao = 0
    
    while opcao != '2':  
        print("-------------- Gestão Loja de Jogos Gui -------------------")
        print('1 - Encontrar todos os documentos')  #
        print('2 - Sair')     

        opcao = input('Informe o que deseja fazer: ') 
        
        if opcao == '1':
            consultar_dados.consultar_todos_dados()
        elif opcao == '2':
            print("Saindo do menu de consulta...")
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
