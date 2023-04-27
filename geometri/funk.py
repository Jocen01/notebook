import math
import numpy as np

import matplotlib.pyplot as plt

from scipy.signal import square, gausspulse

from scipy.integrate import quad

from math import* #import all function from math
x=np.arange(-np.pi,np.pi,0.001) #x axis has been chosen from –π to +π, value 
#of 1 smallest square along x axis is 0.001 

def actual(x):
    res = []
    for i in x:
        if i < 0:
            res.append(0)
        else:
            res.append(sin(i)) 
    r = np.array(res)
    return r

def summ(iter):
    tot = 0
    for i in iter:
        tot += i
    return tot

def fourier(Xcords,times):
    assert times > 0
    if times == 1: return np.array([1/np.pi for _ in times])
    res = [] 
    for i in Xcords:
        res.append(1/np.pi+sin(i)/2+summ([(1-math.pow(-1,k+1))/(np.pi*(1-k**2))*cos(k*i) for k in range(2,times)]))
    return np.array(res)

def up2(x):
    res = []
    for i in x:
        if i== 0 or i == 2*np.pi or i == -2*np.pi:
            res.append(-np.pi)
        elif 0 < i%np.pi <= np.pi - 2:
            res.append(0)
        else:
            res.append(np.pi)
    return np.array(res)

def fourier2(Xcords,times):
    assert times > 0
    if times == 1: return np.array([2 for _ in times])
    res = [] 
    for i in Xcords:
        res.append(2+2*summ([math.pow(-1,k)*sin(2*k)*cos(k*i)/(k) for k in range(1,times)]))
    return np.array(res)

        
y=actual(x)

plt.plot(x,fourier(x,2),'g')
plt.plot(x,fourier(x,6),'r')
plt.plot(x,fourier(x,500),'b')
plt.plot(x,y,'r--')

plt.title("fourier series for \nf(t) = 0 when -pi < t <= 0 and\n f(t) = sin(t) when 0 < t <= pi. \nwith a period of 2*pi")

plt.show()


