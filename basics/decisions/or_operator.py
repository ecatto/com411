print("What type of adventure should I have?")
type = input()

if (type.lower() =="scary") or (type.lower() =="short"):
  print("Entering the dark forest!")

elif (type.lower()) == "safe" or (type.lower() == "long") :
  print("Taking the safe route!")

else :
  print("Not sure which route to take")