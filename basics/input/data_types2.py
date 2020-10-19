#ask user name
print("What is your name human?")
name =input()

#ask user age
print("How old are you (in years)?")
age = input()

#ask user height
print("How tall are you (in meters)?")
height = float(input())

#ask user weight
print("How much do you weigh (in kilograms)?")
weight =float(input())

#calculate bmi
bmi=weight/(height*height)

#display user info
#print(str(name) +"you are",int(age),"years old and your bmi is",round(bmi,2))

#display user info alternative 3
print(str(name),"you are",int(age),"years old and your bmi is {:.2f}" .format(bmi))