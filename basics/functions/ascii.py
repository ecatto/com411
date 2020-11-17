def run():
  print("Program Started!")
  print("Please enter a standard character:")
  character = input()

  if len(character) == 1 :
    print("The ASCII code for {} is {}".format(character,ord(character)))

  else :
    print("Please enter a single character")

  print("Program Ended!")
