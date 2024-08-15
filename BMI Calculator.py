Name = input("Enter your Name: ")

Weight = float(input("Enter your Weight (kg): "))

Height = float(input("Enter your Height (M): "))

BMI = (Weight)/(Height*Height)

if BMI>0:
    if(BMI<20):
        print(Name + " You are underweight.")
    elif(BMI<25):
        print(Name + " You are norml weight.")
    elif(BMI<30):
        print(Name + " You are overwight.")
    elif(BMI<35):
        print(Name + " You are obese.")
    else:
        print(Name + " You are severely obese.")

else:
    print("Enter valid input")


print(Weight)
print(Height)
print(BMI)