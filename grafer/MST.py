
def MST():  #Minimum Spanning Tree
    N = 0                               # antalet noder i grafen
    G = []                              # grafen "lista med kanter [w,u,v] w=vikt, från u till v"
    parent = [-1 for _ in range(N+1)]   # lista föreldernod -> barnnod
    children = [1 for _ in range(N+1)]  # lista barnnod -> föräldernod
    #Det nedan är fungerande kod men långsammare 
    #parent = {}     # dict föreldernod -> barnnod
    #children = {}   # dict barnnod -> föräldernod
    #for i in range(N + 1):
    #    parent[i] = -1
    #    children[i] = 1

    kruskal(G,parent,children,N)

def find(v,parent):
    p = v
    while parent[p] != -1:
        p = parent[p]
    while parent[v] != -1:
        w = parent[v]
        parent[v] = p
        v = w
    return p

def union(u, v, parent, children):
    u = find(u, parent)
    v = find(v, parent)
    if u == v: return
    if children[u] < children[v]:
        parent[u] = v
        children[v] = children[v] + children[u]
    else:
        parent[v] = u
        children[u] = children[v] + children[u]

def kruskal(G, parent,N,children):
    weight = 0
    B = 0
    for w, u, v in G:
        if find(u,parent) != find(v,parent):
            #T.append([u,v]) # lista med kanter i grafen
            union(u,v, parent, children)
            weight += w
            B += 1
        if B == N - 1:  
            break
    return weight

