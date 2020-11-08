print("Program Started!")
print("Please enter an ASCII code:")
reply = int(input())

if reply in range (32,127,1) :
  print("The character represented by the ASCII code {} is {} ".format(reply,chr(reply)))  #and {character} is the ASCII character represented by the number")

print("Program Ended!")