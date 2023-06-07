import random
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    #function
    return y
def find(f,a,b,tolerance):
    max_n = 20
    n = 0;
    x1 = 2
    x2 = 1
    while (x2<=x1):
        x1 = random.uniform(-2,2)
        x2 = random.uniform(-2,2)
    err = abs(f((x1+x2)/2))
    while err > tolerance:
        err = abs(f((x1+x2)/2))
        n += 1
        x1 = x1 - f(x1)*(x1-x2)/(f(x1)-f(x2))
        print('n, [a,b], mid, err = (%2d, [%.5f %.5f], %.5f'% (n,x1,x2,err))
        if (n >= max_n):
            print("Cannot find roots")
            return None
        if (f(x1) == 0):
            return x1
    return x1
x=np.linspace(-2,2,1000)
y=f(x)
plt.plot(x,y)
plt.grid(True)
print('root = ', find(f,-2,2,0.0001))
