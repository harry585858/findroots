import random
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    #function
    return y
def bisection(f,tolerance):
    max_n = 20
    n = 0;
    err = 1
    x1 = random.uniform(-2,2)
    while err > tolerance:
        n += 1
        x1 = x1 - f(x1)/((f(x1+0.0001)-f(x1-0.0001))/0.0002)
        err = abs(f(x1))
        print('n, [a], err = (%2d, [%.5f], %.5f' %(n,x1,err))
        if (n >= max_n):
            print("Cannot find roots")
            return None
    return x1
x=np.linspace(-2,2,1000)
y=f(x)
plt.plot(x,y)
plt.grid(True)
plt.show()
print('root = ', bisection(f,0.0001))
