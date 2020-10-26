#The program should begin by displaying the message "What level of brightness is required?".
#The program should then read in the user's response (an even number representing the brightness level)

print("What level of brightness is required?")
bright = int(input())

print("Adjusting brightness...")

for count in range (0,bright,2) :
  print("\nBeep's brightness level:","*"*(count+2)) 
  print("Bop's brightness level:","*"*(count+2))

print("\nAdjustments complete!")
