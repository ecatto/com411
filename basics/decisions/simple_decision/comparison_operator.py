def run():
  print("Please enter the first number")
  num_one = int(input())

  print("Please enter the second number")
  num_two = int(input())

  if (num_one < num_two) :
    print("The first number is the smallest")
  elif (num_one > num_two) :
    print("The second number is the smallest")
  else :
    print("Both numbers are equal")