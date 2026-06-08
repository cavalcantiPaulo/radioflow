import os

from fila_musicas import adicionar_musica, mostrar_programacao
from historico import tocar_proxima, mostrar_historico
from ranking import curtir_musica, mostrar_ranking


def limpar_tela():
    # Executa o comando de limpar o terminal 
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para continuar...")


def menu():
    while True:
        limpar_tela()

        print("\n========================")
        print("        RADIOFLOW       ")
        print("========================")
        print("1 - Adicionar música")
        print("2 - Tocar próxima música")
        print("3 - Mostrar programação")
        print("4 - Curtir música atual")
        print("5 - Mostrar histórico")
        print("6 - Mostrar ranking")
        print("0 - Sair")

        try:
            opcao = int(input("\nEscolha: "))
        except ValueError:
            # Captura apenas erro de digitação (letras) e joga um valor inválido
            opcao = -1  

        # Dicionário simulando um "Switch-Case" para mapear as ações do menu
        funcoes = {
            1: adicionar_musica,
            2: tocar_proxima,
            3: mostrar_programacao,
            4: curtir_musica,
            5: mostrar_historico,
            6: mostrar_ranking
        }

        # Verifica e executa a função mapeada direto pelo dicionário
        if opcao in funcoes:
            funcoes[opcao]()
            pausar()
        elif opcao == 0:
            print("Sistema encerrado.")
            break
        else:
            print("❌ Opção inválida!")
            pausar()

# Inicializa o programa
menu()