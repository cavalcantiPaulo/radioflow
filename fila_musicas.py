from collections import deque

fila_musicas = deque()

def adicionar_musica():
    titulo = input("Título da música: ")
    artista = input("Artista: ")

    musica = {
        "titulo": titulo,
        "artista": artista
    }

    fila_musicas.append(musica)

    print("✅ Música adicionada com sucesso!")

def mostrar_programacao():
    if not fila_musicas:
        print("Nenhuma música na programação.")
        return

    print("\n=== PROGRAMAÇÃO DA RÁDIO ===")

    for indice, musica in enumerate(fila_musicas, start=1):
        print(
            f"{indice}. {musica['titulo']} - {musica['artista']}"
        )