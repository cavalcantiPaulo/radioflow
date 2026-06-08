import heapq
import historico

# Dicionário de frequência para contar as curtidas
curtidas = {}

def curtir_musica():
    if historico.musica_atual is None:
        print("Nenhuma música está tocando.")
        return

    titulo = historico.musica_atual["titulo"]

    if titulo not in curtidas:
        curtidas[titulo] = 0

    curtidas[titulo] += 1
    print("👍 Curtida registrada!")


def mostrar_ranking():
    if not curtidas:
        print("Nenhuma curtida registrada.")
        return

    # Fila de Prioridade (Heap) para fazer a ordenação eficiente
    heap = []

    # HEAPUSH: Como heapq cria uma Min-Heap por padrão, usamos o valor NEGATIVO para simular uma Max-Heap (maior curtida no topo)
    for musica, quantidade in curtidas.items():
        heapq.heappush(heap, (-quantidade, musica))

    print("\n🏆 RANKING DAS MAIS CURTIDAS")
    posicao = 1

    # HEAPPOP: Extrai sempre o elemento de maior prioridade (mais curtido)
    while heap:
        quantidade, musica = heapq.heappop(heap)

        # Invertemos o sinal novamente (-quantidade) para exibir o número positivo real
        print(f"{posicao}. {musica} ({-quantidade} curtidas)")
        posicao += 1