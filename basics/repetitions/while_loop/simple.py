def run():
  #The program should start by displaying the message
  #The program should then read in the user's response
  print("How many cables should I remove?")
  answer = int(input())

  #The program should then create a variable to track the number of removed cables and set this to 0.
  count = int(0)

  #The program should then use a while loop to do the following:
  #    Display the message "Removed cable."
  #    Increment the variable for tracking the number of removed cables
  while (count < answer) :
    print("Removed cable")
    count = count+1
