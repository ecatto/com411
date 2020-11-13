def box(word):
  print((len(word)+4)*"*")
  print(  "* {} *".format(word))
  print((len(word)+4)*"*")

def lowercase(word):
  print(word.lower())

def uppercase(word):
  print(word.upper())

def mirror(word):
  print(word,"| ", end="")
  for count in range (len(word)-1,-1,-1):
    print (word[count], end="")

def repeat(word):
  print("How many times would you like the word repeated?")
  times = int(input())
  for count in range (0,times,1):
    if (count%2==1):
      lowercase(word)
    else:
      uppercase(word)


#Beep and Bop wish to create a program which manipulate cryptic words. 
def run ():
  print("Please enter a word")
  response = input()

  print("""Please choose one of the following options:

  1) Display in a Box
  2) Display Lower-case – display the word in lower-case 
  3) Display Upper-case – display the word in upper-case 
  4) Display Mirrored – display the word with its mirrored word
  5) Repeat """)

  choice = int(input())

  if choice ==1:
    box(response)
  elif choice ==2:
    lowercase(response)
  elif choice ==3:
    uppercase(response)
  elif choice == 4:
    mirror(response)
  elif choice ==5:
    repeat(response)
  else:
    print("Please enter a number between 1 and 5")
#The program should then read the option number entered by the user and carry out the appropriate actions.

#The program should contain 6 user-defined functions. One for each of the above options and one to run the program. 
run()