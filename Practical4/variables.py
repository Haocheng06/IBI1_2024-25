a=15    # a is time of walking to bus stop
b=1*60+15    # b is time of bus journal
c=a+b   # calculate the total time of taking bus
d=1*60+30 # d is time of driving
e=5 # e is time of walking from car parking 
f=d+e # calculate the total time of driving
if c>f :
    print("driving is faster")
else:
    print("bus is faster")
# because c==90min and f==95min, so c>f taking bus is faster.
X=True
Y=False
W=X and Y    
print(W)
# X      Y      W
# True   Flase  Flase
# Flase  True   Flase 
# Flase  Flase  Flase 
# True   True   True