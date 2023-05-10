import math
import random
from ObjectiveFunctions import *

class Firefly:
    def __init__(self, index, position, dim=2, lower=-10, upper=10):
        self.index = index
        self.position = position
        self.attract = 0
        self.fitness = 0
        self.dim = dim
        self.lower = lower
        self.upper = upper
        
        
        
        
        
    def __str__(self):
        return f"({self.index}) {self.position}"
    
    def __lt__(self, other):
        # print(f"{self.fitness} < {other.getFitness()}?")
        return self.fitness < other.getFitness()

    
    def getPosition(self):
        return self.position
    
    def calculateAttractiveness(self):
        pass
    
    def calculateFitness(self):
        # the initial function to be optimized
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
    
    def move(self, other, attractiveness, alpha):
        # for dim in range(self.dim):
        #     self.position[dim] = self.position[dim] + attractiveness * (other.getPosition()[dim] - self.position[dim]) + stepSize
        self.position = self.position + attractiveness * (other.getPosition() - self.position) + alpha * (random.random()-0.5)
        self.checkBoundary()
            
    def moveRandom(self, alpha):
        # for dim in range(self.dim):
        #     self.position[dim] = self.position[dim] + stepSize
        self.position = self.position + (alpha * (random.random()-0.5))
        
    def checkBoundary(self):
        for dim in range(self.dim):
            if self.position[dim] < self.lower:
                self.position[dim] = self.lower
            if self.position[dim] > self.upper:
                self.position[dim] = self.upper
                
            
            
    
    
        
        
    