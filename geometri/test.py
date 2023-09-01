# representerar en linje i a,b,c
import math, time


#def linje(p1,p2):
#    a = -p2[1] - p1[1]
#    b = p2[0] - p1[0]
#    c = p1[0]*p2[1] - p1[1]*p2[0]
#    return (a,b,c)

def pts2line(p, q):
    return (-q[1] + p[1],
          q[0] - p[0],
          p[0]*q[1] - p[1]*q[0])

#GCD
def GCD(a, b):
    if(b == 0):
        return abs(a)
    else:
        return GCD(b, a % b)

def dist(p1,p2):
    return math.sqrt(math.pow(p1[1]-p2[1],2)+math.pow(p1[0]-p2[0],2))

def polygon(points):
    points.sort(key= lambda a : a[0])
    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def polygonArea(points):
    import math
    if len(points) < 3:
        return 0
    pre = points[-1]
    summ = 0
    for p in points:
        summ += pre[0]*p[1]-pre[1]*p[0]
        pre = p
    return math.fabs(summ) / 2

def perimeter(points): # returns the length of the perimiter of a polygon
    t1 = time.time_ns()
    import math
    if len(points) < 3:
        return 0
    pre = points[-1]
    summ = 0
    for p in points:
        summ += math.sqrt(math.pow(pre[0]-p[0],2)+math.pow(pre[1]-p[1],2))
        pre = p
    print(time.time_ns() - t1)
    return summ

def point_in_polygon(P, points):# 0 -> outside, 1 -> inside, 2 -> on the edge
    import math     # based on https://math.stackexchange.com/questions/2460414/how-to-determine-if-a-ray-intersects-a-line   

    def pts2line(p, q):
        return (-q[1] + p[1],
            q[0] - p[0],
            p[0]*q[1] - p[1]*q[0])
    
    def cross(a, b):
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]
        return c
    
    def distl(l, p):
        return (abs(l[0]*p[0] + l[1]*p[1] + l[2])
        /math.hypot(l[0], l[1]))
    
    crossings = 0
    V = [743,1327] # direction of ray with origin p
    # the purpose of the next segment is to make sure the ray doesn't pass trou any points. ae, passing trou points breaks the algoritm
    line = pts2line(P,[P[0]+V[0],P[1]+V[1]])
    if [1 for p1 in points if p1 == P]: return 2
    while [1 for p in points if distl(line, p) == 0]: 
        V = [V[0]+1,V[1]+1] #generates a line with no points on the polygon on it
        line = pts2line(P,[P[0]+V[0],P[1]+V[1]])
    
    crosss = cross(P+[1],[V[0],V[1],0])

    for i in range(len(points)):
        p1,p2 = points[i-1], points[i]
        Q = cross(cross(p1+[1],p2+[1]),crosss)

        if Q[2] != 0:
            if (Q[0]/Q[2]-P[0]) > 0 or (Q[1]/Q[2]-P[1]) > 0: # comparissons are only acurate for a line with Vx, Vy both positive
                if min(p1[0],p2[0]) < Q[0]/Q[2] < max(p1[0],p2[0]) or min(p1[1],p2[1]) < Q[1]/Q[2] < max(p1[1],p2[1]):
                    crossings += 1
            
            elif Q[0]-P[0]*Q[2] == 0 and Q[1]-P[1]*Q[2] == 0:
                if min(p1[0],p2[0]) < Q[0]/Q[2] < max(p1[0],p2[0]) or min(p1[1],p2[1]) < Q[1]/Q[2] < max(p1[1],p2[1]):
                    return 2
        
    return crossings%2

_,P = input()
points = [[float(p) for p in input().split("# ")[1].split()] for _ in range(P)]
perimeter(points)