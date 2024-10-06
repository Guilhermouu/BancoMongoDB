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
           
        elif opcao == '2':
                inserir_dados.inserir_dados()
                
        elif opcao == '3':
                menu_consultar.menuconsultar()

        elif opcao == '4':
                menu_update.menu_update()

        elif opcao == '5':
               menu_deletar.menu_deletar()

        elif opcao == '6':
                break
main()