class Fenwic:
    def __init__(self,N) -> None:
        self.data = [0]*(N+1)

    def sum(self,i):
        #i += 1
        acc = 0
        while i > 0:
            acc += self.data[i]
            i -= (i&-i)
        return acc

    def inc(self,i,delta):
        k = 1
        if self.sum(i) > self.sum(i-1):
            k = -1
        #i += 1
        
        
        while i < len(self.data):
            self.data[i] += delta * k
            i += (i&-i)

    def quarry(self,l,r):
        return self.sum(r) - self.sum(l-1)