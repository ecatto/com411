def run():
  #The program should begin by displaying the message 

  print("How far are we from the cave?")
  answer = int(input())

  for count in range (answer):
    print(answer,"steps remaining")
    answer =answer -1
