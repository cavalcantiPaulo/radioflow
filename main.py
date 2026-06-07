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

        try:
            opcao = int(input("\nEscolha: "))
        except:
            opcao = ""

        funcoes = {
            1: adicionar_musica,
            2: tocar_proxima,
            3: mostrar_programacao,
            4: curtir_musica,
            5: mostrar_historico,
            6: mostrar_ranking
        }

        if opcao in funcoes.keys():
            funcoes[opcao]()
            pausar()

        elif opcao == 0:
            print("Sistema encerrado.")
            break

        else:
            print("❌ Opção inválida!")
            pausar()

menu()