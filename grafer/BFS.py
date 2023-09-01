#Graph = [[1,2,3],[0],[0,3],[0,4],[3,7],[7],[7],[4,5,6]]
#0, 1,1,1,2,4,4,3

def bfs(Graph, S):
    q = [S]
    dist = {S: 0}
    while q:
        q2 = []
        for u in q:
            for v in Graph[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q2.append(v)
        q = q2
    return dist


Graph = [[1, 2, 3], [0], [0, 3], [0, 4], [3, 7], [7], [7], [4, 5, 6]]
dists = bfs(Graph, 0)

print(dists)


def bfs2(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    q = [(r, c)]
    dist = {(r, c): 0}
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if grid[nr, nc] != '#' and tup not in dist:
                        dist[tup] = dist[r, c] + 1
                        q2.append(tup)
        q = q2
    return dist


grid = {}


def bfs(Graph, S):
    q = [S]
    dist = {S: 0}
    while q:
        q2 = []
        for u in q:
            for v in Graph[u]:
                if v not in dist:
                    dist[v] = (dist[u] + 1)%2
                    q2.append(v)
                else:
                    assert dist[v] != dist[u]
        q = q2
    return dist