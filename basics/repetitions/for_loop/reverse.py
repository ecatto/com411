def run():
  #The program should begin by displaying the message
  print("What phrase do you see?")
  phrase = input()

  print("reversing...")

  for count in range (len(phrase)-1,-1,-1):
    print (phrase[count], end="")
