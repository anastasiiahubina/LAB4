import heapq
from collections import defaultdict

def find_min_time(n, a, b, routes):
    graph = defaultdict(list)
    for s, ts, f, tf in routes:
        # Перевірка меж та допустимості даних
        if 0 <= s < n and 0 <= f < n and ts < tf:
            graph[s].append((ts, f, tf))
    
    min_time = [float('inf')] * n
    min_time[a] = 0

    heap = [(0, a)]  # (current_time, current_city)

    while heap:
        curr_time, u = heapq.heappop(heap)

        if u == b:
            return curr_time

        if curr_time > min_time[u]:
            continue

        for ts, f, tf in graph[u]:
            if ts >= curr_time and tf < min_time[f]:
                min_time[f] = tf
                heapq.heappush(heap, (tf, f))

    return -1 if min_time[b] == float('inf') else min_time[b]

# Читання входу
if __name__ == "__main__":
    try:
        n = int(input())
        a, b = map(int, input().split())
        r = int(input())
        routes = []
        for _ in range(r):
            parts = input().strip().split()
            if len(parts) == 4:
                s, ts, f, tf = map(int, parts)
                routes.append((s, ts, f, tf))
        print(find_min_time(n, a, b, routes))
    except Exception:
        print(-1)  # У разі будь-якої помилки повернути -1