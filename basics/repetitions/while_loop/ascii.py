#The program should start by displaying the message 
#The program should then read in the user's response.
print("How many bars should be charged?")
answer = int(input())

#The program should then create a variable to track the number of bars charged and set this to 0.
count = 0

#The program should then use a while loop to do the following:
#    Display the message "Charging:".
#    Increment the variable for tracking the number of charged bars.
#    Display the number of charged bars.

while (count < answer) :
  count = count +1
  print("\nCharging: ","█ "*count)

#Finally, the program should display the message 
print("\nThe battery is fully charged.")
