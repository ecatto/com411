#line 5 overwrites whole dictionary

def pattern():
  #creates and inits dictionary
  sequences = {"Short Sequence":3}  
  #line 6 overwrites whole dictionary
  sequences = {"Short - Sequence":4}  
  #adds or overwrites single specificed element
  sequences["wibble"]=7
  #adds or overwrites multiple specified elements
  sequences.update({"Short Sequence":5, "Medium Sequence":2, "Long Sequence":1})

  return sequences

def run():
  print(pattern())

run()
