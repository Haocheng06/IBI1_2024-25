#create a dictionary containing all data
#import the plt model
#draw the bar according to the data in the dictionary
#show the bar
#input what language's percentage user want to know
#print the desired percenntage according to the dictionary

#create dict
dic={ 'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5}

#lead in the model
import matplotlib.pyplot as plt

#get keys of dict as x-axis data
x=list(dic.keys())

#get values of dic as y-axis data
y=list(dic.values())

#draw the bar
plt.bar(x,y)

#label x-axis as "language type"
plt.xlabel('language type')

#give the bar a title
plt.title('language popularity')

#label y-axis as popularity
plt.ylabel('popularity')

#show the figure
plt.show()

#get what language popularity want to know
per=input("what language user percentage do you want to know? ")

#get the desired language popularity according the dic and print it
print(dic[per])    
    