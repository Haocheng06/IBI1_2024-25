import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/IBI-practical/IBI_2024-25/Practical10")
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
# print(dalys_data.head(5))
# print(dalys_data.info())
dalys_des=dalys_data.describe()
# print(dalys_des)


max_dalys=max(dalys_data.iloc[0:,3])
min_dalys=min(dalys_data.iloc[0:,3])
first_year=min(dalys_data.iloc[0:,2])
recent_year=max(dalys_data.iloc[0:,2])
print(f"Max dalys is {max_dalys}")
print(f"Min dalys is {min_dalys}")
print(f"first year is {first_year}")
print(f"the recent year is {recent_year}")



first_ten_rows=dalys_data.iloc[0:10,2] 
print(first_ten_rows)     # the 10th year with DALYs data recorded in Afghanistan: 1999


    
print(dalys_data.loc[dalys_data["Year"]==1990,"DALYs"])
    



france=dalys_data.loc[dalys_data.Entity=="France",["DALYs","Year"]]
uk=dalys_data.loc[dalys_data.Entity=="United Kingdom",["DALYs","Year"]]

mean_france=sum(france.DALYs)/len(france.Year)
mean_uk=sum(uk.DALYs)/len(uk.Year)
print(f"the mean DALYs of the UK is bigger is {mean_uk>mean_france}") # the UK's mean DALYs is bigger 
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.show()




uk=dalys_data.loc[dalys_data.Entity=="United Kingdom",["DALYs","Year"]]
china=dalys_data.loc[dalys_data.Entity=="China",["DALYs","Year"]]
plt.plot(uk.Year, uk.DALYs, 'b+',label="UK")
plt.plot(china.Year,china.DALYs,'r+', label="CHina")
plt.xticks(uk.Year,rotation=-90)
plt.legend()
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.show()
