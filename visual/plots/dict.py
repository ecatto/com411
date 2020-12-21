import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  print("What type of line would you like (:, -- or -)?")
  line=input()
  print("What colour would you like (r, g or b)?")
  colour=input()
  print("What style of marker would you like (o, s or ^) ?")
  marker=input()

  paths["line"]=line
  paths["colour"]=colour
  paths["marker"]=marker

  return paths

def generate():
  print("How many lines would you like to display?")#
  num_lines = int(input())
  for count in range (num_lines):
    values = data()
    x=rnd.sample(range(0,20),5)
    y=rnd.sample(range(0,20),5)
    wibble=(f"{values['marker']}{values['line']}{values['colour']}")
    plt.plot(x,y, wibble)
      
  plt.show()

def run():
  print( "Running....")
  generate()
  print("Done!")

run()