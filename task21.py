def calculate_BMI(weight_Kg,height_m):
    return weight_Kg / (height_m ** 2)
print("weight_Kg :" ,calculate_BMI(90,188))
print("weight_g :" ,calculate_BMI(90000,188))
