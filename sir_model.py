#import packages
import numpy
import scipy.integrate
import matplotlib.pyplot as plt

def differential_equation(y, time, beta, gamma):

    """
    differential equation
    =====================
    A function that takes as parameter the initial value (y), the time,
    the betta which is the coefficiant of decrease the number of susceptible and
    gamma which is the coefficiant we use with the recovered differential equation.

    return : This function returns an array with ds/di, di/dt and dr/dt.
    """

    S, I, R = y
    ds_dt = -beta * S * I
    di_dt = beta * S * I - gamma * I
    dr_dt = gamma * I
    return ([ds_dt, di_dt, dr_dt])

#initial condition
initialS = 200
initialI = 29
initialR = 10

So = initialS
Io = initialI
Ro = initialR

beta = 0.35
gamma = 0.15

#time vector
time = numpy.linspace(0, 100, 100000)

#sir_model
sir_model = scipy.integrate.odeint(differential_equation, [So, Io, Ro], time, args = (beta, gamma))
sir_model = numpy.array(sir_model)

#plot result
#plt.figure(figsize[6, 4])
plt.plot(time, sir_model[:, 0], label = "S(t)")
plt.plot(time, sir_model[:, 1], label = "I(t)")
plt.plot(time, sir_model[:, 2], label = "R(t)")
plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("proportion")
plt.show()
