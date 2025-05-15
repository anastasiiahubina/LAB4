class DSU:
    def init(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    # Сортуємо ребра за вагою
    edges.sort(key=lambda x: x[2])  # x = (u, v, weight, original_index)

    for u, v, w, idx in edges:
        if dsu.union(u, v):
            mst_weight += w
            mst_edges.append(idx)
        if len(mst_edges) == n - 1:
            break

    if len(mst_edges) != n - 1:
        return -1, []
    return mst_weight, sorted(mst_edges)  # Відсортуй для стабільного виводу

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    edges = []

    index = 2
    for i in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        w = int(data[index + 2])
        edges.append((u, v, w, i + 1))  # зберігаємо індекс ребра (1-based)
        index += 3

    weight, mst = kruskal(n, edges)
    if weight == -1:
        print(-1)
    else:
        print(weight)
        for i in mst:
            print(i)

if __name__ == "__main__":
    main()