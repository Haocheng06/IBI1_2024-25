# get user's height and weight 
# calculate the BMI according to the formula
# if BMI is over 30 then print overweight
# if BMI is in range between 18.5 and 30,print normal
# if BMI is under 18.5,print underweight 

height=float(input("input your height in m ")) # Prompt the user to input their height in meters and convert the input to a floating - point number
weight=float(input("input your weight in kg "))# Prompt the user to input their weight in kilograms and convert the input to a floating - point number
BMI=weight/height**2 #calclate BMI using the formula weight
print("You BMI is", BMI) # Print the calculated BMI value
if BMI>=30: # Check if the BMI is greater than or equal to 30
    print ("You are overweight!") #If the condition is true, print a message indicating the person is overweiht
elif BMI>=18.5: # Check if the BMI is greater than or equal to 18.5 (but less than 30)
    print("Your BMI is in normal range, congratulations!") #If the condition is true, print a message indicating a normal BMI range
else:
    print("You are underweight!") # If neither of the above conditions are true, print a message indicating the person 