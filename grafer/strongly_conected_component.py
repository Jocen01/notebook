
def kosaraju(adj):
    n = len(adj)
    scc = []
    part_of = [0] * n
    stack = []

    def dfs(adj, order, first_iteration):
        visited = [False] * n
        dfs_stack = []
        for node in order:
            if not visited[node]:
                visited[node] = True
                dfs_stack.append((node, 0))
                if not first_iteration:
                    scc.append([])
                while dfs_stack:
                    (node, next) = dfs_stack.pop()
                    visited[node] = True
                    if next == len(adj[node]):
                        if first_iteration:
                            stack.append(node)
                        else:
                            part_of[node] = len(scc) - 1
                            scc[-1].append(node)
                    else:
                        dfs_stack.append((node, next + 1))
                        if not visited[adj[node][next]]:
                            dfs_stack.append((adj[node][next], 0))

    dfs(adj, range(n), True)

    adj_rev = [[] for _ in range(n)]
    for (a, adj) in enumerate(adj):
        for b in adj:
            adj_rev[b].append(a)

    dfs(adj_rev, reversed(stack), False)

    is_dag = n == len(scc)
    return (scc, part_of, is_dag)