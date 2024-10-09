import banco_dados
import menu_principal
import inserir_dados
import menu_consultar
import menu_update
import menu_deletar
def main():
 while True:
        opcao= menu_principal.menu()
                
        if opcao == '1':
           banco_dados.conectar_banco()
           #função que conecta ao banco de dados
        elif opcao == '2':
                inserir_dados.inserir_dados()
                #função que insere dados no banco
        elif opcao == '3':
                menu_consultar.menuconsultar()
                #menu que consulta todos os dados no banco e que tem a função de consultar
        elif opcao == '4':
                menu_update.menu_update()
                #menu que atualizar todos os dados no banco e que tem a função de atualizar dados no banco
        elif opcao == '5':
               menu_deletar.menu_deletar()
                #menu que deleta todos os dados no banco e que tem aa funçao de deletar dados no banco
        elif opcao == '6':
                break
                #opção de break caso o usúario aperte 6
main()