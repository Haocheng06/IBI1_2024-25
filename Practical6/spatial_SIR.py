# Initialize parameters and population
# Set beta, gamma, time_point
# Create 100x100 population array filled with 0s
# Randomly set one individual as infected

# // Time-step loop
# For t from 0 to time_point - 1
#    Find infected individuals' indices
#    Create a copy of the population (new_population)

#    For each infected individual
#       Decide if it recovers
#        If recovers, mark as recovered in new_population
#        Else
#            For each neighbor
#                Check if neighbor is susceptible
#                If susceptible, decide if it gets infected
#                If infected, mark as infected in new_population

#    Update population with new_population

#    // Plot at specific time steps
#   If t in [0, 10, 50, 99]
#        Plot population state


import numpy as np
import matplotlib.pyplot as plt
population=np.zeros((100,100))
outbreak = np.random. choice(range(100) ,2)
population[outbreak[0], outbreak[1]] = 1
plt.figure(figsize=(6,4),dpi=150)

beta=0.3
gamma=0.05
time_point=100
for t in range(time_point):
    infected=np.where(population==1)
    new_population = population.copy()
    for i in range(len(infected[0])):
        x,y=infected[0][i],infected[1][i]
        p=np.random.choice([True,False],p=[gamma,1-gamma])
        if p ==True:
            new_population[x,y]=2
        else:
            for dx in(-1,0,1):
                for dy in(-1,0,1):
                    if dx==0 and dy==0:
                        continue
                    else:
                        new_x=x+dx
                        new_y=y+dy
                        if 0<=new_x<100 and 0<=new_y<100 and population[new_x,new_y]==0:
                            q=np.random.choice([True,False],p=[1-beta,beta])
                            if q==True:
                                continue
                            else:
                                new_population[new_x,new_y]=1
                        else:
                            continue
    population=new_population
    if t in [0, 10, 50, 99]:
            plt.imshow(population, cmap='viridis', interpolation='nearest')
            plt.title(f'Time: {t}')
            plt.colorbar()
            plt.show()
