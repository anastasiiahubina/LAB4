import sys
sys.setrecursionlimit(1 << 25)

class DSU:
    def init(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.color = [0] * n  # 0 or 1 for bipartite coloring

    def find(self, x):
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.color[x] ^= self.color[orig_parent]
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return self.color[x] != self.color[y]  # If they are in same component, they must have different color
        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.color[ry] = self.color[x] ^ self.color[y] ^ 1  # Flip color to maintain bipartite condition
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    
    dsu = DSU(n)
    result = []
    idx = 2
    is_bipartite = True

    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        if is_bipartite:
            if not dsu.union(u, v):
                is_bipartite = False
        result.append('1' if is_bipartite else '0')

    print(''.join(result))

if __name__ == "__main__":
    main()