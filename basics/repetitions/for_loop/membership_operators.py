#The program should begin by displaying the message
print("What phrase do you see?")
phrase = input()

print("reversing...")

phrase_2 = ""

for letter in phrase:
  phrase_2 = letter + phrase_2

print(phrase_2)


