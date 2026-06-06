import os

from fila_musicas import (
    adicionar_musica,
    mostrar_programacao
)

from historico import (
    tocar_proxima,
    mostrar_historico
)

from ranking import (
    curtir_musica,
    mostrar_ranking
)

def limpar_tela():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pausar():
    input("\nPressione Enter para continuar...")

def menu():

    while True:

        limpar_tela()

        print("\n========================")
        print("      RADIOFLOW")
        print("========================")
        print("1 - Adicionar música")
        print("2 - Tocar próxima música")
        print("3 - Mostrar programação")
        print("4 - Curtir música atual")
        print("5 - Mostrar histórico")
        print("6 - Mostrar ranking")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            adicionar_musica()
            pausar()

        elif opcao == "2":
            tocar_proxima()
            pausar()

        elif opcao == "3":
            mostrar_programacao()
            pausar()

        elif opcao == "4":
            curtir_musica()
            pausar()

        elif opcao == "5":
            mostrar_historico()
            pausar()

        elif opcao == "6":
            mostrar_ranking()
            pausar()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("❌ Opção inválida!")
            pausar()

menu()