def Drug_dosage_calculator(weight,concentration):
    drug_concentration=[120/5,250/5]
    recommended_dose=15
    if concentration not in drug_concentration:
        return("Your drug concentration is not correct!")
    else:
        if weight<10:
            return("Weight Error")
        elif weight>100:
            return("Weight Error")
        else:
            drug_mass=weight*recommended_dose
            drug_volume=drug_mass/concentration
            
            return drug_volume 
test_weight=30
test_concentration=120/5
test_volume=Drug_dosage_calculator(test_weight,test_concentration)
print(f"The test is well done, with 30kg and 120mg/5ml, and the tested volume is {test_volume}")


a=int(input("Enter your weihgt: "))
b=int(eval(input("Enter your drug concentration: ")))
print(f"According to your weight and drug concentreation, you need to intake {Drug_dosage_calculator(a,b)} ml drug")