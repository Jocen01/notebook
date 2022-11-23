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

def getLongestPathDAG(DAG, graph):
    path = {DAG[0]: (1,-1)}
    f = (1, DAG[0])
    FR = DAG[0]
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