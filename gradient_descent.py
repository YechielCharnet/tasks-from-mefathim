import matplotlib.pyplot as plt
import numpy as np

def data_file():
    data_xy = np.load('XYdata.npz')
    return data_xy

def main():
    data_xy = data_file()
    x = data_xy['array_1.npy']
    y = data_xy['array_2.npy']
    t1 = 500
    t2 = 500
    g = 0.0001
    n = len(x)
    for i in range(20000):
        f_t1 = 0
        f_t2 = 0
        for i in range(n):
            f_t1 += (t1+t2*x[i]-y[i])
            f_t2 += ((x[i])*(t1+t2*x[i]-y[i]))
        if abs(max(f_t1, f_t2)) < g:
            break
        t1 = t1-g*f_t1*2/n
        t2 = t2-g*f_t2*2/n
        
    print(t1, t2)
    x1 = np.array([x.min(), x.max()])
    y1 = t2*x1+t1
    plt.plot(x1, y1)
    plt.plot(x, y)
    plt.scatter(x, y)
    plt.show()

if __name__=='__main__':
    main()

