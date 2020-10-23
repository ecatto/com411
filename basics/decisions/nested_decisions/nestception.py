print ("Where should I look?")
response = input()

if (response.lower() == "in the bedroom"):
  print ("Where in the bedroom should I look?")
  answer = input()
  if (answer.lower() == "under the bed") :
    print("Found some shoes but no battery")
  else :
    print ("Found some mess but no battery.")

elif (response == "in the bathroom"):
  print("Where in the bathroom should I look?")
  answer = input()
  if (answer.lower() == "in the bathtub") :
    print("Found a rubber duck but no battery")
  else :
    print ("Found a wet surface  but no battery.")

elif (response == "in the lab"):
  print("Where in the lab should I look?")
  answer = input()
  if (answer.lower() == "on the table") :
    print("Yes! I found my battery!")
  else :
    print ("Found some tools but no battery.")


