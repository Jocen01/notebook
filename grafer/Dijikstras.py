from heapq import heappush, heappop
# s : startNod
#g: [[(to_node,wight), ... ] , ...]
INF = 10**18


def dijkstra(s, T, G):
    dists = [INF]*len(G)
    parent = [None]*len(G)
    heap = []
    heappush(heap, (0, s))
    dists[s] = 0
    while heap:
        d, u = heappop(heap)
        if u == T:
            return d  # när man vill gå från s till t
        if d > dists[u]:
            continue
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                parent[v] = u
                heappush(heap, (alt, v))

    if dists[T] == INF:
        return None
    path = []
    curr = T
    while curr != None:
        path.append(curr)
        curr = parent(curr)

    # return path[::-1]
    return dists


G = [[(1, 3), (2, 1)], []]
