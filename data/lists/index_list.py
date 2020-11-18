def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  var=movements()
  for count in range (len(var)):
    if (count%2 ==1):
      print(" for",var[count], "steps")
    else:
      print(var[count], end="")

def run2():
  print("Moving...")
  var=movements()
  for count in range (0,len(var),2):
      print("{} for {} steps".format(var[count],var[count+1]))

run()
run2()
