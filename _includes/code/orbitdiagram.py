import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import matplotlib as mpl

def logisticMap(x,r):
    # Applies the "map" function f in logistic map
    return r*x*(1-x)

def iterateLogisticMap(x0,nsteps,r):
    # Applies the logistic map recursively to initial
    # point x0 for nsteps using parameter r, and
    # returns an array of (r,x) values.
    xlist = np.zeros([nsteps,2])
    xlist[0,:] = [r,x0]
    x = x0
    for i in range(nsteps):
        x = logisticMap(x,r)
        xlist[i,:] = [r,x]
    return xlist

def orbitDiagramPoints(rmin,rmax,N_r,N_x):
    # Takes as input a range of r values over which to
    # iterate the map forward by 2*N_x steps. The variable
    # N_r controls the density of points in the r-direction.
    # Then, it keeps the last N_x points. This ensures
    # that transients die out and we are left with a "grid" of
    # N_x points in the vertical direction and N_r points
    # in the horizontal direction.
    r_vals = np.linspace(rmin,rmax,N_r)
    points_grid = np.zeros([len(r_vals),N_x,2])
    for i,r in enumerate(r_vals):
        points = iterateLogisticMap(rand(),2*N_x,r)
        keep_points = points[-N_x:]
        points_grid[i,:,:] = keep_points
    return points_grid

def makeOrbitDiagram(rmin,rmax,N_r,xmin,xmax,Nsteps):
    # Does not output anything; generates an orbit diagram.
    points_list = orbitDiagramPoints(rmin,rmax,N_r,Nsteps).reshape(-1,2)
    plt.figure(figsize=(6,6),dpi=300)
    plt.scatter(points_list[:,0],points_list[:,1],s=0.1)
    plt.xlim(rmin,rmax)
    plt.ylim(xmin,xmax)
    # plt.gca().set_aspect(0.8)
    plt.xlabel("Parameter r")
    plt.ylabel("Variable x")
    plt.title("Orbit Diagram for Logistic Map")
    plt.savefig(f"OrbitDiagram_x{xmin}-{xmax}r{rmin}-{rmax}.png")
    plt.show()

    
print("Use this module to run the function: ")
print("makeOrbitDiagram(rmin,rmax,N_r,xmin,xmax,Nsteps)")
