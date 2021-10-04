import numpy as np
import matplotlib.pyplot as plt

from cblind.cblind import Colorplots, mapping

def test_cblind(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().cblind(ny)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=1.5)

    plt.show()

def test_huescale(ny, *args):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().huescale(ny, *args)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_rbscale(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().rbscale(ny)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_rainbow(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().rainbow(ny)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_monocolor(ny, *args):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().monocolor(ny, *args)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=1.0)

    plt.show()

def test_mapping(palette=None,nbin=None):
    fig, ax = plt.subplots()

    r = np.arange(-np.pi, np.pi, 0.1)
    t = np.arange(0, 2*np.pi, 0.1)
    X, Y = np.meshgrid(r, t)
    data = np.cos(X) * np.sin(Y) * 10

    mapping(fig, ax, data, palette=palette, nbin=nbin)
    plt.show()
