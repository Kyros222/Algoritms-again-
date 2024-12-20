import heapq
import time
import sys
sys.setrecursionlimit(1000000)
def prim_with_heap(graph):
    start_vertex = next(iter(graph))
    mst = []
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]
    heapq.heapify(edges)
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst





def prim_without_heap(graph):
    start_vertex = next(iter(graph))
    mst = []
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]
    while edges:
        edges.sort()
        cost, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    edges.append((cost, to, to_next))
    return mst

def test_prim_algorithms():
    num_nodes = 12310
    graph = {i: {} for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph[i][j] = graph[j][i] = i + j

    start_time = time.time()
    mst_with_heap = prim_with_heap(graph)
    time_with_heap = time.time() - start_time

    start_time = time.time()
    mst_without_heap = prim_without_heap(graph)
    time_without_heap = time.time() - start_time

    print(f"Time with heap: {time_with_heap:.5f} s")
    print(f"Time without heap: {time_without_heap:.5f} s")
#----------------------------------------------------------------
test_prim_algorithms()