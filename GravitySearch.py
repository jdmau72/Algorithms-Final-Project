import random
import math
from Agent import Agent
import matplotlib.pyplot as plt
import time




# HYPER-PARAMETERS --------------
IS_MIN_OPT = True
NUM_AGENTS = 100
INIT_RANGE_MIN = -10
INIT_RANGE_MAX = 10
G_0 = 6.8     # based on recommended 2018 value for G
# G_0 = 10
ALPHA = -25
EPSILON = 0.5
T = 50    # max number of iterations
DIMENSIONS = 2


    
def findMin(agents):
    min = agents[0]
    for agent in agents:
        if (agent.getFitness() < min.getFitness()):
            min = agent
    
    return min


def findMax(agents):
    max = agents[0]
    for agent in agents:
        if (agent.getFitness() > max.getFitness()):
            max = agent
    
    return max


def calculate_sum_m(agents):
    sum_m = 0
    for agent in agents:
        sum_m += agent.get_m()

    return sum_m


# initialization of things
agentsList = []
t = 1       # this iteration
plt.xlim(INIT_RANGE_MIN, INIT_RANGE_MAX)
plt.ylim(INIT_RANGE_MIN, INIT_RANGE_MAX)


# Step 1
# Generate initial population
print("\nStep 1")
for i in range(NUM_AGENTS):
    x1_i = random.randrange(INIT_RANGE_MIN, INIT_RANGE_MAX)
    x2_i = random.randrange(INIT_RANGE_MIN, INIT_RANGE_MAX)
    
    agentsList.append(Agent(i, [x1_i, x2_i], dim=DIMENSIONS))
    agentsList[i].evalFitness()
    
print(agentsList)
if (IS_MIN_OPT):
        best = findMin(agentsList)
else:
        best = findMax(agentsList)
        
print(f"Original Best at {best.getPosition()}: {best.getFitness()}")


# for testing use the examples provided by the paper
# agentsList.append(Agent(0, [-5, 0], dim=DIMENSIONS))
# agentsList.append(Agent(1, [0, 2], dim=DIMENSIONS))
# agentsList.append(Agent(2, [-2, 3], dim=DIMENSIONS))
# agentsList.append(Agent(3, [5, 5], dim=DIMENSIONS))
# agentsList.append(Agent(4, [0, 4], dim=DIMENSIONS))
# ------------------------------------------------------------------------- 

while (t != T):

    # Step 2
    # Evaluate fitness for each agent
    print("\nStep 2")
    for agent in agentsList:
        agent.evalFitness()
        # print(f"Fitness of Agent ({agent}):  {agent.evalFitness()}")
    # -------------------------------------------------------------------------    


    # Step 3 
    # Update the G, best, and worst of the population
    if (IS_MIN_OPT):
        best = findMin(agentsList)
        worst = findMax(agentsList)
    else:
        best = findMax(agentsList)
        worst = findMin(agentsList)
        
    # print(f"Best: {best.getFitness()}")
    # print(f"Worst: {worst.getFitness()}")

    G = G_0 * (math.e)**(ALPHA * (t/T))
    # print(f"G: {G}")
    # -------------------------------------------------------------------------    



    # Step 4 
    # Calculate M, F_ij, and a for each agent
    # print("\n\n Calculating mass, forces, and acceleration ----------------------------")
    for agent in agentsList:    # calculate m_i
        agent.calculate_m(best.getFitness(), worst.getFitness())
        # print(f"{agent} _m_ : {agent.get_m()}")

    sum_m = calculate_sum_m(agentsList)

    for agent in agentsList:    # calculate M_i
        agent.calculate_M(sum_m)
        # print(agent.get_M())


    # NEED TO FIX HOW IT ITERATES THROUGH!!!!
    # pairs = [(a, b) for idx, a in enumerate(agentsList) for b in agentsList[idx + 1:]]
    # for (agent_i, agent_j) in pairs:
    #     # calculate Euclidian distance R_ij
    #     R_ij = math.dist(agent_i.getPosition(), agent_j.getPosition())
    #     print(f"{agent_i}, {agent_j}: R_ij = {R_ij}")
    #     for dim in range(DIMENSIONS):   # calculate F_ij in each dimension
    #         # MAYBE LOOK IN HERE FOR DEBUGGING I DONT KNOW WHY THIS OPT SUCKS
    #         F_ij = ((G * agent_i.get_M() * agent_j.get_M()) / (R_ij + EPSILON)) * (agent_j.getPosition()[dim] - agent_i.getPosition()[dim])
    #         agent_i.addForce(dim, F_ij)
    #         agent_j.addForce(dim, F_ij)
    #         print(f"        F_{dim+1}_ij = {F_ij}")
    #     print()
    #####
    
    
    
    # FIXED VERSION (hopefully)
    for i in range(len(agentsList)):
        for j in range(len(agentsList)):
            if (i != j):
                agent_i = agentsList[i]
                agent_j = agentsList[j]
                
                # calculate Euclidian distance R_ij
                R_ij = math.dist(agent_i.getPosition(), agent_j.getPosition())
                # print(f"{agent_i} pulled by {agent_j}: R_ij = {R_ij}")
                for dim in range(DIMENSIONS):   # calculate F_ij in each dimension
                    # MAYBE LOOK IN HERE FOR DEBUGGING I DONT KNOW WHY THIS OPT SUCKS
                    F_ij = ((G * agent_i.get_M() * agent_j.get_M()) / (R_ij + EPSILON)) * (agent_j.getPosition()[dim] - agent_i.getPosition()[dim])
                    agent_i.addForce(dim, F_ij)
                    # agent_j.addForce(dim, F_ij)
                    # print(f"        F_{dim+1}_ij = {F_ij}")
                # print()
    
    
    
    
        
    # calculate F and a for each agent
    for agent in agentsList:
        # print(agent)
        agent.calculate_F()     # both calculate for each dim and print
        agent.calculate_a()
        

        
        
        


    # Step 5 
    # Update velocity and position
    # print("\n\n Updating velocity and position ----------------------------")
    for agent in agentsList:
        # print(agent)
        agent.update_v()
        agent.update_position()

    
    # if no, loop to step 2
    for agent in agentsList:
        agent.resetForces()
        
        # plot the agents on a graph
        plt.plot(agent.getPosition()[0], agent.getPosition()[1], 'o', color='black')
    plt.draw()
    plt.pause(0.00001)
    plt.clf()
    
    plt.xlim(INIT_RANGE_MIN, INIT_RANGE_MAX)
    plt.ylim(INIT_RANGE_MIN, INIT_RANGE_MAX)
        
    t += 1
    
    
        

# should have OPT now
print(f"\n\n\nFinally, we have found OPT at {best.getPosition()}: {best.getFitness()}")
print(f"OPT: {((1 + 2*3 -7)**2 + (2*1 + 3 - 5)**2)}")