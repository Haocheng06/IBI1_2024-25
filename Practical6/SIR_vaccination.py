import numpy as np
import matplotlib.pyplot as plt

V_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
N=10000
beta=0.3
gamma=0.05
time=1000

for rate in V_rate:
    S_array=[]
    R_array=[]
    I_array=[]
    V_array=[]
    I=1
    R=0
    V=int(N*rate)
    S=N-R-I-V
    recover_possibility=gamma
    for i in range(time):
        if N!=V:
            infect_possibility=beta*(I/(N-V))
        else:
            infect_possibility=0
        if S>0:
            new_infected=sum(np.random.choice(range(2),S,p=[1-infect_possibility,infect_possibility]))
        else:
            S=0
        new_recover=sum(np.random.choice(range(2),I,p=[1-recover_possibility,recover_possibility]))
        if S>=new_infected:
            S-=new_infected
        else:
            S=0
        if I>=0:
            I=I+new_infected-new_recover
        else:
            I=0
        R+=new_recover
        S_array.append(S)
        I_array.append(I)
        R_array.append(R)
        
    plt.plot(I_array,label=str(rate))

plt.figure(figsize=(6,4),dpi=150)
plt.xlabel("time")
plt.ylabel("infected population")
plt.title("Vaccination_SIR model")
plt.legend()
plt.show()

