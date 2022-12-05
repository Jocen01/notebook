def createDAG(graph,nodes):
    DAG = []
    prosesed = set()
    prosesing = []   
    for i in nodes:
        if i in prosesed: continue
        prosesing.append(i)
        while prosesing:
            p = prosesing[-1]
            for to in graph[p]:
                if to not in prosesed:
                    prosesing.append(to)
            if p == prosesing[-1]:
                p = prosesing.pop()
                DAG.append(p)
                prosesed.add(p)
    return DAG

def topSort(graph,nodes):
    from collections import defaultdict
    DAG = []
    state = defaultdict(lambda: 0)
    prosesing = []  
    for i in nodes:
        if state[i] == 2: continue
        prosesing.append(i)
        state[i] = 1
        while prosesing:
            p = prosesing[-1]
            for to in graph[p]:
                if state[to] == 1:
                    return []
                if state[to] != 2:
                    prosesing.append(to)
                    state[to] = 1
                    break
            if p == prosesing[-1]:
                p = prosesing.pop()
                DAG.append(p)
                state[p] = 2
    return DAG

def getLongestPathDAG(DAG, graph):
    path = {DAG[0]: (1,-1)} #dict with the node -> next node 
    f = (1, DAG[0]) # f[0] is the length of the longest path in dag
    FR = DAG[0] # FR is the point at witch the longest path begins
    for i in DAG:
        if i in path: continue
        longest = (1,-1)
        for to in graph[i]:
            temp = path[to]
            if temp[0] + 1 > longest[0]:
                longest = (temp[0] + 1, to)
        path[i] = longest
        if f[0] < longest[0]:
            f = longest
            FR = i
    return path, f, FR