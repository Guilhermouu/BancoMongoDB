
import deletar_um

def menu_deletar():
 opcao=0
 while opcao != '2':
        print("-------------- Gestão Loja de Jogos Gui -------------------")
        print('1- Deletar um Documento')
        print('2- Sair')
        opcao=input('Informe o que deseja fazer: ') 
               
        if opcao == '1':
            deletar_um.deletar_um()
        