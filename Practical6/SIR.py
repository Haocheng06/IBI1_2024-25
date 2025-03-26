import numpy as np
import matplotlib.pyplot as plt
S=9999
I=1
R=0
N=10000
beta=0.3
gamma=0.05
S_array=[S]
I_array=[I]
R_array=[R]
time=1000    
for i in range(time):
    infect_possibility=beta*(I/N)
    recover_possibility=gamma 
    new_infected=sum(np.random.choice(range(2),S,p=[1-infect_possibility,infect_possibility]))#if here the sum is a float, what will go on?
    new_recover=sum(np.random.choice(range(2),I,p=[1-recover_possibility,recover_possibility]))
    S-=new_infected
    I=I+new_infected-new_recover
    R+=new_recover
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_array,label="Susceptible")    
plt.plot(I_array,label="Infected")
plt.plot(R_array,label="Recover")
plt.xlabel("time")
plt.ylabel("population")
plt.title("SIR model")
plt.legend()
plt.show()
plt.savefig("C:/IBI/IBI_2024-25/Practical6")
