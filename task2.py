import heapq
from collections import defaultdict

def min_cost(n, fuel_costs, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    INF = float('inf')
    min_costs = [INF] * n
    min_costs[0] = 0

    heap = [(0, 0)]  # (total_cost, current_city)

    while heap:
        cost, city = heapq.heappop(heap)
        if cost > min_costs[city]:
            continue
        for neighbor in graph[city]:
            new_cost = cost + fuel_costs[city]
            if new_cost < min_costs[neighbor]:
                min_costs[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return -1 if min_costs[n - 1] == INF else min_costs[n - 1]

# Читання даних для dОТС
if __name__ == "__main__":
    try:
        n = int(input())
        fuel_costs = list(map(int, input().split()))
        m = int(input())
        roads = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
        print(min_cost(n, fuel_costs, roads))
    except Exception:
        print(-1)