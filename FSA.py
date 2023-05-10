import random
import math
from Firefly import Firefly
import matplotlib.pyplot as plt
import time
import numpy as np
from ObjectiveFunctions import *





# HYPER-PARAMETERS --------------
IS_MIN_OPT = True
NUM_AGENTS = 100
INIT_RANGE_MIN = -10
INIT_RANGE_MAX = 10
T = 50   # max number of iterations
DIMENSIONS = 2
GAMMA = 0.9
# GAMMA = 0.01
# B_0 = 5
B_0 = 4
ALPHA = 0.001


def calculateAttractiveness(x1, x2):
    return B_0 * math.e **(-1 * GAMMA * (math.dist(x1.getPosition(), x2.getPosition()))**2)
    
# def calculateIntensity(x1, x2):
#     return x1.getFitness() * math.e **(-1 * GAMMA * (math.dist(x1, x2))**2)

def boothFunction(x, y):
    return ((x + 2*y -7)**2 + (2*x + y - 5)**2)

 
# # define range for input
# r_min, r_max = INIT_RANGE_MIN, INIT_RANGE_MAX
# # sample input range uniformly at 0.1 increments
# xaxis = np.arange(r_min, r_max, 0.1)
# yaxis = np.arange(r_min, r_max, 0.1)
# # create a mesh from the axis
# x, y = np.meshgrid(xaxis, yaxis)
# # compute targets
# results = boothFunction(x, y)
# # create a filled contour plot with 50 levels and jet color scheme
# plt.contourf(x, y, results, levels=50, cmap='jet')

# # show the plot
plt.show()


# initialization of things
fireflies = []
t = 1       # this iteration
plt.xlim(INIT_RANGE_MIN, INIT_RANGE_MAX)
plt.ylim(INIT_RANGE_MIN, INIT_RANGE_MAX)
plt.suptitle('Gravity Search Algorithm')




# Step 1
# Generate initial population
print("\nStep 1")
for i in range(NUM_AGENTS):
    x1_i = random.randrange(INIT_RANGE_MIN, INIT_RANGE_MAX)
    x2_i = random.randrange(INIT_RANGE_MIN, INIT_RANGE_MAX)
    
    fireflies.append(Firefly(i, np.array([x1_i, x2_i]), dim=DIMENSIONS, lower=INIT_RANGE_MIN, upper=INIT_RANGE_MAX))
    
print(fireflies)

# for testing use the examples provided by the paper
# agentsList.append(Agent(0, [-5, 0], dim=DIMENSIONS))
# agentsList.append(Agent(1, [0, 2], dim=DIMENSIONS))
# agentsList.append(Agent(2, [-2, 3], dim=DIMENSIONS))
# agentsList.append(Agent(3, [5, 5], dim=DIMENSIONS))
# agentsList.append(Agent(4, [0, 4], dim=DIMENSIONS))
# ------------------------------------------------------------------------- 

while (t != T):

    
    plt.clf()
    plt.xlim(INIT_RANGE_MIN, INIT_RANGE_MAX)
    plt.ylim(INIT_RANGE_MIN, INIT_RANGE_MAX)
    plt.suptitle('Firefly Algorithm')
    
    # Step 2
    # Calculate fitness for each firefly
    for firefly in fireflies:
        firefly.calculateFitness()
    
 
    for i in range(1, NUM_AGENTS - 1):
        noneBrighter = True
        for j in range(1, NUM_AGENTS - 1):
            if (IS_MIN_OPT):
                if (fireflies[j] < fireflies[i]):
                    # now update that fireflies position
                    attractiveness = calculateAttractiveness(fireflies[i], fireflies[j])
                    fireflies[i].move(other=fireflies[j], attractiveness=attractiveness, alpha=ALPHA)
                    fireflies[i].calculateFitness()
                    noneBrighter = False
            else:
                if (fireflies[j] > fireflies[i]):
                    # now update that fireflies position
                    attractiveness = calculateAttractiveness(fireflies[i], fireflies[j])
                    fireflies[i].move(other=fireflies[j], attractiveness=attractiveness, alpha=ALPHA)
                    fireflies[i].calculateFitness()
                    noneBrighter = False
        if (noneBrighter==True):
            fireflies[i].moveRandom(alpha=ALPHA)
            fireflies[i].calculateFitness()

            
    
    # plot the agents on a graph
    for firefly in fireflies:
        # plot the agents on a graph
        # plt.contourf(x, y, results, levels=50, cmap='jet')
        plt.plot(firefly.getPosition()[0], firefly.getPosition()[1], 'o', color='black')
    plt.draw()
    plt.pause(0.000001)
    

        
        
    t += 1
    
# find best of fireflies
best = fireflies[0]
for firefly in fireflies:
    if (IS_MIN_OPT):
        if firefly < best:
            best = firefly
    else:
        if firefly > best:
            best = firefly
    
# # define range for input
r_min, r_max = INIT_RANGE_MIN, INIT_RANGE_MAX
# # sample input range uniformly at 0.1 increments
xaxis = np.arange(r_min, r_max, 0.1)
yaxis = np.arange(r_min, r_max, 0.1)
# # create a mesh from the axis
x, y = np.meshgrid(xaxis, yaxis)
# # compute targets
print(x, y)
results = objective(x, y)
# # create a filled contour plot with 50 levels and jet color scheme
plt.contourf(x, y, results, levels=50, cmap='jet')
plt.figtext(0.5, 0.03, f"Experimental OPT: {best.getFitness()}", ha="center", fontsize=7)
plt.figtext(0.5, 0.01, f"True OPT: {0}", ha="center", fontsize=7)
plt.savefig(f'Firefly {OBJECTIVE_FUNCTION}_.png')



# should have OPT now
print(f"\n\n\nFinally, we have found OPT at {best.getPosition()}: {best.getFitness()}")
print(f"OPT: {((1 + 2*3 -7)**2 + (2*1 + 3 - 5)**2)}")