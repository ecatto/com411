import matplotlib.pyplot as plt

def tri():
  wibble = {}
  wibble["x"] = [1,3,2,1]
  wibble["y"] = [1,1,3,1]
  wibble["marker"] = "s"
  wibble["line"] = "--"
  wibble["colour"] = "r"

  formatted = f"{wibble['marker']}{wibble['line']}{wibble['colour']}"
  plt.plot(wibble["x"], wibble["y"], formatted)
  plt.show()

tri()