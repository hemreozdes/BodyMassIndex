gender= input("Enter your gender:(M/W)")
age= int(input("Enter your age:"))
height= float(input('Enter your height(m):'))
weight= float(input("Enter your weight(kg):"))
bsa= 0.20247*(height**0.725)*(weight**0.425)  #Body Surface Area
bmi= weight/height**2                        #Body Mass Index
if(bmi<18.5):
    print("Skinny!")
elif(18.5<=bmi<25):
    print("Normal!")
elif(25<=bmi<30):
    print("Overweight!")
elif(30<=bmi<35):
    print("1st degree obesity!")
elif(35<=bmi<40):
    print("2st degree obesity!")
elif(40<=bmi):
    print("3st degree morbid obesity!")
if(gender=="M"):
    idealW=print("Your ideal weight is ",(height-100+age/10)*0.9)
    lbm=(1.1*weight-128*(weight**2))/(100*(height**2))  
    print(f"Your lean body mass value is {lbm:.4f}")
if(gender=="W"):
    idealW=print(f"Your ideal weight is ",(height-100+age/10)*0.8)
    lbm=(1.07*weight-148*(weight**2))/(100*(height**2))
    print(f"Your lean body mass value is {lbm:.4f}")