height=float(input("input your height in m "))
weight=float(input("input your weight in kg "))
BMI=weight/height**2
print("You BMI is", BMI)
if BMI>=30:
    print ("You are so heavy!")
elif BMI>=18.5:
    print("Your BMI is in normal range, congratulations!")
else:
    print("You are so thin!")