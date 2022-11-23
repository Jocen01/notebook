# representerar en linje i a,b,c
import math


def linje(p1,p2):
    a = -p2[1] - p1[1]
    b = p2[0] - p1[0]
    c = p1[0]*p2[1] - p1[1]*p2[0]
    return (a,b,c)

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

def perimeter(points):
    import math
    if len(points) < 3:
        return 0
    pre = points[-1]
    summ = 0
    for p in points:
        summ += math.sqrt(math.pow(pre[0]-p[0],2)+math.pow(pre[1]-p[1],2))
        pre = p
    return summ