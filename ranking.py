import heapq
import historico

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

    heap = []

    for musica, quantidade in curtidas.items():
        heapq.heappush(
            heap,
            (-quantidade, musica)
        )

    print("\n🏆 RANKING DAS MAIS CURTIDAS")

    posicao = 1

    while heap:
        quantidade, musica = heapq.heappop(heap)

        print(
            f"{posicao}. "
            f"{musica} "
            f"({-quantidade} curtidas)"
        )

        posicao += 1