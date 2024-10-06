
import atualizar_dados
def menu_update():
      opcao = 0 
    
      while opcao != '2':  
        print("-------------- Gestão Loja de Jogos Gui -------------------")
        print('1 - atualizar documentos')  #
        print('2 - Sair')     

        opcao = input('Informe o que deseja fazer: ') 
        
        if opcao == '1':
            atualizar_dados.atualizar_jogo()
        elif opcao == '2':
            print("Saindo do menu de consulta...")
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
