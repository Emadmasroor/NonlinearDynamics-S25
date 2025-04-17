import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz_rhs(t,state,s,r,b):
    # Break up state variable into 3:
    x,y,z = state

    dxdt = s*(y-x)
    dydt = r*x - y - x*z
    dzdt = x*y - b*z

    # Assemble
    return [dxdt,dydt,dzdt]

    # Initial condition
y0 = [0.9, 0.0, 0.0]

# Time span for the solution (start time, end time)
t_span = (0, 50)

# Plot the solution at the following times:
tvals = np.linspace(0,t_span[1],10000)

# Solve the ODE
solution1 = solve_ivp(lorenz_rhs, # system of equations
                      t_span, # time span of integration
                      y0, # initial conditions
                      args=(10,28,8/3), # parameters
                      t_eval=tvals, # times at which to store solution
                      method='RK45' # method of integration
                     )

fig1 = plt.figure(dpi=100,figsize=(12,5))

# 3-d plot
ax1_1 = fig1.add_subplot(1,2,1, projection='3d')
ax1_1.plot(solution1.y[0], solution1.y[1], solution1.y[2], lw=0.5, color='black')
ax1_1.set_title("Solution in [x,y,z] space ")

# time-trace
ax1_2 = fig1.add_subplot(1, 2, 2)
ax1_2.set_aspect(1/2)
ax1_2.plot(solution1.t, solution1.y[2], lw=0.5, color='blue')
ax1_2.set_title("Variable 'z' against time")

plt.show()