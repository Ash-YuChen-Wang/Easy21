import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_value(v):
    x, y = np.mgrid[1:22, 1:11]
    z = v[x - 1, y - 1]
    ax = plt.subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.coolwarm, alpha=0.8)
    ax.set_xlabel('Player sum')
    ax.set_ylabel('Dealer showing')
    ax.set_zlabel('Value function')
    plt.show()

def mse(x,y):
    squared = (x-y)**2
    return squared.mean()

def mse_lambda(mse):
    x = [i/10 for i in range(0,11)]
    plt.plot(x,mse)
    plt.xlabel('Lambda')
    plt.ylabel('MSE')
    plt.show()