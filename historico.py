from fila_musicas import fila_musicas

# Pilha para armazenar o histórico
pilha_historico = [] 
musica_atual = None

def tocar_proxima():
    global musica_atual

    if len(fila_musicas) == 0:
        print("A fila está vazia. Nada para tocar no momento.")
        return

    # Retira a próxima música da fila
    musica_atual = fila_musicas.popleft()

    # PUSH: Adiciona no topo do histórico
    pilha_historico.append(musica_atual)

    print(f"\n▶️ Tocando agora: {musica_atual['titulo']} (de {musica_atual['artista']})")


def mostrar_historico():
    if not pilha_historico:
        print("O histórico está vazio.")
        return

    print("\n--- HISTÓRICO ---")

    # Cópia para iterar com 'pop' sem apagar o histórico original
    pilha_temp = pilha_historico.copy()
    
    posicao = 1
    
    while pilha_temp:
        # POP: Remove e retorna o último elemento
        musica = pilha_temp.pop()
        
        print(f"{posicao}º | {musica['titulo']} - {musica['artista']}")
        posicao += 1