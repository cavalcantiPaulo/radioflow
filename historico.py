from fila_musicas import fila_musicas

historico = []
musica_atual = None

def tocar_proxima():
    global musica_atual

    if not fila_musicas:
        print("Nenhuma música na fila.")
        return

    musica_atual = fila_musicas.popleft()

    historico.append(musica_atual)

    print(
        f"\n🎵 Tocando: "
        f"{musica_atual['titulo']} - {musica_atual['artista']}"
    )

def mostrar_historico():

    if not historico:
        print("Histórico vazio.")
        return

    print("\n=== HISTÓRICO ===")

    copia_historico = historico.copy()

    indice = 1

    while copia_historico:

        musica = copia_historico.pop()

        print(
            f"{indice}. "
            f"{musica['titulo']} - {musica['artista']}"
        )

        indice += 1