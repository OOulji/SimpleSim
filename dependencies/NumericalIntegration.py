import numpy as np 

#Numerical methods for integration.

def EulerODE(t,y0,fun):

#  Euler method integration. 
# -------------------------------------------
#  * t is the vector (array) containing the independent variable values where the ODE is to be evaluated.
#  * y0 is the initial value for the problem. 
#  * fun is the f(t,y) function obtained when the EDO is expressed as y' = f(t,y)

    y = np.zeros(len(t)) #y values for the ODE. 
    y[0] = y0 #Initial condition is the first value of the array.

    #Euler integration:

    for i in range(len(t)-1):
        y[i+1] = y[i] + (t[i+1]-t[i])*fun(t[i],y[i])
    return y

#Same as previus, but it takes a 2D vector as the initial conditions

def EulerODE2D(t, y0:np.array ,fun):

    y = np.zeros([len(t),2]) #y values for the ODE. 
    y[0] = y0[0]
    y[1] = y0[1] #Initial condition is the first value of the array.

    for i in range(len(t)-1):
        y[i+1,0] = y[i,0] + (t[i+1]-t[i])*fun(t[i],y[i,0])
        y[i+1,1] = y[i,1] + (t[i+1]-t[i])*fun(t[i],y[i,1])
    return y

# RK4 integration (classic Runge-Kutta method) for 1st order ODE.
# -------------------------------------------
#  * t is the vector (array) containing the independent variable values where the ODE is to be evaluated.
#  * y0 is the initial value for the problem. 
#  * fun is the f(t,y) function obtained when the EDO is expressed as y' = f(t,y)

def RK4(t,y0,fun):

    y = np.zeros(len(t))
    y[0] = y0

    h = t[1]- t[0]
        
    for i in range(len(t)-1):

        k1 = fun(t[i],y[i])
        k2 = fun(t[i]+h/2, y[i] + h*(k1/2))
        k3 = fun(t[i]+h/2, y[i] + h*(k2/2))
        k4 = fun(t[i]+h , y[i] + h*k3)

        y[i+1] = y[i] + (1/6)*h*(k1+2*k2+2*k3+k4)

    return y

#RK4 integration (classic Runge-Kutta method) for 2nd order ODE.
# -------------------------------------------
#  * t is the vector (array) containing the independent variable values where the ODE is to be evaluated.
#  * y0 and z0 are the initial values for the problem. 
#  * f and g are the resulting functions when separating the 2nd order ODE in a system of two first order ODEs

def RK4_2ndOrder(t,y0,z0,f,g):

    y = np.zeros(len(t))
    y[0] = y0
    z = np.zeros(len(t))
    z[0] = z0

    h = h = t[1]- t[0]

    for i in range(len(t)-1):
    
        k1 = f(t[i], y[i], z[i])
        l1 = g(t[i], y[i], z[i])

        k2 = f(t[i]+h/2, y[i] + h*(k1/2), z[i] + h*(l1/2))
        l2 = g(t[i]+h/2, y[i] + h*(k1/2), z[i] + h*(l1/2))

        k3 = f(t[i]+h/2, y[i] + h*(k2/2), z[i] + h*(l2/2))
        l3 = g(t[i]+h/2, y[i] + h*(k2/2), z[i] + h*(l2/2))

        k4 = f(t[i]+h , y[i] + h*k3, z[i] + h*l3)
        l4 = g(t[i]+h , y[i] + h*k3, z[i] + h*l3)

        y[i+1] = y[i] + (1/6)*h*(k1+2*k2+2*k3+k4)
        z[i+1] = z[i] + (1/6)*h*(l1+2*l2+2*l3+l4)

    results = np.array([[y],[z]])

    return results



