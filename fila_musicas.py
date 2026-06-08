from collections import deque

# Fila (FIFO) utilizando deque para gerenciar a programação
fila_musicas = deque()

def adicionar_musica():
    titulo = input("Título da música: ")
    artista = input("Artista: ")

    musica = {
        "titulo": titulo,
        "artista": artista
    }

    # ENQUEUE: Adiciona a música no final da fila
    fila_musicas.append(musica)

    print("✅ Música adicionada com sucesso!")


def mostrar_programacao():
    # Verifica se a fila está vazia
    if not fila_musicas:
        print("Nenhuma música na programação.")
        return

    print("\n=== PROGRAMAÇÃO DA RÁDIO ===")

    # Percorre a fila do início para o fim (Ordem FIFO) sem destruir os dados
    for indice, musica in enumerate(fila_musicas, start=1):
        print(f"{indice}. {musica['titulo']} - {musica['artista']}")