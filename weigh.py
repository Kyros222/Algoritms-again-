class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    def connected(self, x, y):
        return self.find(x) == self.find(y)






if __name__ == "__main__":
    import random
    import time

    size = 228334
    uf = UnionFind(size)

    start_time = time.time()
    for _ in range(size):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
        uf.union(a, b)
    print(f"Time:{time.time() - start_time:.4f} s")

    start_time = time.time()
    for _ in range(228334):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
        uf.connected(a, b)
    print(f"Time: {time.time() - start_time:.4f} s")