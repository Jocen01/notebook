def miller_rambin(N):
    A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] #räcker för upp till 10**18 annars är det bara lägga till några fler primtal
    d = N - 1
    s = 0
    if N < 100: #kolla de låga primtalen
        for i in range(2,N):
            if N%i == 0:
                return False
        return True
    if N % 2 == 0:
        return False
    while d % 2 == 0:
        s+= 1
        d = d//2
    # Miller–Rabin primality test
    for a in A:
        X = pow(a, d, N)
        Y = 1
        for _ in range(s):
            Y = pow(X, 2, N)
            if Y == 1 and X != 1 and X != N - 1:
                return False
            X = Y
        if Y != 1:
            return False
    return True



def primesive(n):
    sive = [1 for _ in range(n*11)]
    sive[0] = 0
    sive[1] = 0
    primes = []
    for i,p in enumerate(sive):
        if p == 1:
            primes.append(i)
            for j in range(i,n*10,i):
                sive[j] = 0
    return primes
    
#GCD
def GCD(a, b):
    if(b == 0): return abs(a)
    return GCD(b, a % b)