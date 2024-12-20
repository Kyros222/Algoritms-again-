import random
import time

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def kruskal_with_union_find(edges, num_nodes):
    edges.sort(key=lambda x: x[2]) 
    uf = UnionFind(num_nodes)
    mst = []
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    return mst

def kruskal_without_union_find(edges, num_nodes):
    edges.sort(key=lambda x: x[2])  
    mst = []  
    connected = [set([i]) for i in range(num_nodes)]

    for u, v, weight in edges:
        set_u = set_v = None
        for s in connected:
            if u in s:
                set_u = s
            if v in s:
                set_v = s
        if set_u != set_v:
            mst.append((u, v, weight))
            connected.remove(set_u)
            connected.remove(set_v)
            connected.append(set_u.union(set_v))
    return mst


def generate_large_test_data(num_nodes, num_edges):
    edges = []
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        weight = random.randint(1, 100)
        edges.append((u, v, weight))
    return edges

def test_kruskal():
    num_nodes = 777
    num_edges = 2323
    edges = generate_large_test_data(num_nodes, num_edges)

    mst_with_union_find = kruskal_with_union_find(edges, num_nodes)
    mst_without_union_find = kruskal_without_union_find(edges, num_nodes)

    print("MST with Union-Find:", len(mst_with_union_find))
    print("MST without Union-Find:", len(mst_without_union_find))

test_kruskal()