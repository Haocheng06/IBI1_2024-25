#create two lists
#sort these two lists
#import the module 
#prepare the list containing different places for later pie
#create the figure and divide it into two subpart 
#create two pie whose data saved in 1 decimal 
#make sure the pie is a circle
#title two figures 
#show these figures at the same time

#create two lists containing the population
uk_countries=[57.11,3.13,1.91,5.45]
Zhejiang_neighbouring=[65.77,41.88,45.28,61.27,85.15]

#sort these two lists and print
uk_countries.sort()
Zhejiang_neighbouring.sort()
print(uk_countries)
print(Zhejiang_neighbouring)

#import the model
import matplotlib.pyplot as plt

#create two lists containing different places 
label1=['England','Wales','Northern Ireland','Scotland']
label2=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']

#create two subspace to make sure two pies can show at the same time 
fig, (ax1, ax2) =plt.subplots(1,2)

#draw the first pie in circle shape and title it
ax1.pie(uk_countries,labels=label1, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')
ax1.set_title('UK countries population')

#draw the second pie in circle and title it 
ax2.pie(Zhejiang_neighbouring,labels=label2,autopct="%1.1f%%",startangle=90)
ax2.axis('equal')
ax2.set_title('Zjejiang neighbouring population')

#adjust the distance between two figures automatically
plt.tight_layout

#show the figures at the same time 
plt.show()