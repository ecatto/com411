
#ask user name
print("What is your name human?")
name =str(input())

#ask user age
print("How old are you (in years)?")
age = int(input())

#ask user height
print("How tall are you (in meters)?")
height = float(input ())

#ask user weight
print("How much do you weigh (in kilograms)?")
weight =float(input())

#calculate bmi
bmi=round(weight/(height*height),2)

#display user info
print((name),"you are",(age),"years old and your bmi is",bmi)