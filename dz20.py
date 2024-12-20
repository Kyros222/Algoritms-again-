
import random
import time
# import sys
# sys.setrecursionlimit(1000000)
#ne obrashayte vnimanie na moy ONGLIYSKII

def belman_ford(versh, rebra, istok):
    dist = [float('inf')] * versh
    dist[istok] = 0
    for _ in range(versh - 1):
        for (u, v, ves) in rebra:
            if dist[u] != float('inf') and dist[u] + ves < dist[v]:
                dist[v] = dist[u] + ves
    for (u, v, ves) in rebra:
        if dist[u] != float('inf') and dist[u] + ves < dist[v]:
            raise ValueError("Граф содержит цикл отрицательного веса")
    
    return dist

def sozdat_graf(versh, max_ves=100):
    rebra = []
    for _ in range(versh * 2):
        u = random.randint(0, versh - 1)
        v = random.randint(0, versh - 1)
        ves = random.randint(-max_ves, max_ves)
        rebra.append((u, v, ves))
    return rebra

def test_belman_ford():
    versh = 100
    rebra = sozdat_graf(versh)
    istok = 0
    




    
    start = time.time()
    try:
        dist = belman_ford(versh, rebra, istok)
        print(f"Shortest distances: {istok}: {dist}")
    except ValueError as e:
        print(e)
    end = time.time()
    print(f"Time: {end - start:.2f} sec")

test_belman_ford()
