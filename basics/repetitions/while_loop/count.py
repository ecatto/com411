def run():
  #The program should start by displaying the message "How many live cables must I avoid?".
  #The program should then read in the user's response.

  print("How many live cables must I avoid?")
  live = int(input())

  #The program should then create a variable to track the number of live cables and set this to 0.
  count= int(0)

  #The program should then use a while loop 
  while (count < live) :
    count = count +1
    print("Avoiding...Done! {} live cables avoided".format(count))

  while (count<live) :
    print("")(count = count +1), print("")

  #Finally, the program should display the message "All live cables have been avoided."

  print("\nAll live cables have been avoided")
