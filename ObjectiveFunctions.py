import math
import matplotlib.pyplot as plt
import numpy as np

 # change this to change the objective function used
OBJECTIVE_FUNCTION = 'Matyas'

def objective(x, y):
    plt.title(f"{OBJECTIVE_FUNCTION} Function")
    
    if (OBJECTIVE_FUNCTION == 'Booth'):
        return boothFunction(x,y)
    elif(OBJECTIVE_FUNCTION == 'Bukin'):
        return bukinFunction(x,y)
    elif(OBJECTIVE_FUNCTION == 'Matyas'):
        return matyasFunction(x,y)
    elif(OBJECTIVE_FUNCTION == 'Schaffer'):
        return schafferFunction(x,y)



def boothFunction(x, y):
    return ((x + 2*y -7)**2 + (2*x + y - 5)**2)

def bukinFunction(x, y):
    return 100 * np.sqrt(np.absolute(y - 0.01 * x**2)) + 0.01 * np.absolute(x + 10)

def matyasFunction(x, y):
    return 0.26 * (x**2 + y**2) - 0.48 * x * y

def schafferFunction(x, y):
    return 0.5 + (np.sin(x**2 - y**2)**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2