import math
import random
from ObjectiveFunctions import *

class Agent:
    def __init__(self, index, position, fitness=0, M=0, m=0, dim=1):
        self.index = index
        self.position = position
        self.fitness = fitness
        self.M = M
        self.m = m
        self.a = []
        self.v = []
        self.F = []
        self.dim = dim
        self.forces = []
        for i in range(dim):
            self.forces.append([])
            self.F.append(0)
            self.a.append(0)
            self.v.append(0)
        # print(self.forces)
        # print(self.F)
        # print(self.a)
        
        
    def __str__(self):
        return f"({self.index}) {self.position}"
        
    # the initial function to be optimized
    def evalFitness(self):
        x1 = self.position[0]
        x2 = self.position[1]
        # print(self.position)
        
        # self.fitness = ((x1**2) + (x2**2))
        self.fitness = objective(x1, x2)
        # self.fitness = bukinFunction(x1, x2)
        # self.fitness = matyasFunction(x1, x2)
        # self.fitness = schafferFunction(x1, x2)
        
        return self.fitness
    
    def getFitness(self):
        return self.fitness
    
    def calculate_m(self, best_t, worst_t):
        self.m = (self.fitness - worst_t) / (best_t - worst_t)
        
    def get_m(self):
        return self.m
    
    def calculate_M(self, sum_m):
        self.M = self.m / sum_m
        
    def get_M(self):
        return self.M
    
    def getPosition(self):
        return self.position
    
    def addForce(self, dim, F_ij):
        self.forces[dim].append(F_ij)
        
    def resetForces(self):
        self.forces = []
        for i in range(self.dim):
            self.forces.append([])
            
    def calculate_F(self):
        for dim in range(self.dim):
            
            sumWeightedForces = 0
            for force in self.forces[dim]:
                sumWeightedForces += force * random.random()
            self.F[dim] = sumWeightedForces
            
            # self.F[dim] = sum(self.forces[dim]) 
            # print(f"    F in dim_{dim+1}: {self.F[dim]}")
            
    def calculate_a(self):
        for dim in range(self.dim):
            if (self.M != 0):
                self.a[dim] = self.F[dim] / self.M
            else:
                self.a[dim] = 0
            # print(f"    a in dim_{dim+1}: {self.a[dim]}")
            
    def update_v(self):
        for dim in range(self.dim):
            self.v[dim] = random.random() * self.v[dim] + self.a[dim] 
            # print(f"    New velocity in dim_{dim+1}: {self.v[dim]}")
            
    def update_position(self):
        for dim in range(self.dim):
            self.position[dim] = self.position[dim] + self.v[dim]
            # print(f"    New x_{dim+1}: {self.position[dim]}")
            
            
