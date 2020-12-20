import matplotlib.pyplot as plt

def small():
  plt.plot([3,4], [3,3], 'ro:')
  plt.plot([3,4], [4,4], 'ro:')
  plt.plot([3,3], [3,4], 'ro:')
  plt.plot([4,4], [3,4], 'ro:')
<<<<<<< HEAD
  #def small():
  #x = [3, 3, 4, 4, 3]
  #y = [3, 4, 4, 3, 3]
  #plt.plot(x, y, 'r:o')
=======
  def small():
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]
  plt.plot(x, y, 'r:o')
>>>>>>> 31d1fbd233fa47773e23b39b8ac1b6af0e3ecec5


def medium():
  plt.plot([2,5], [2,2], 'gs--')
  plt.plot([2,5], [5,5], 'gs--')
  plt.plot([2,2], [2,5], 'gs--')
  plt.plot([5,5], [2,5], 'gs--')


def large():
  plt.plot([1,6], [1,1], 'bp-')
  plt.plot([1,6], [6,6], 'bp-')
  plt.plot([1,1], [1,6], 'bp-')
  plt.plot([6,6], [1,6], 'bp-')
  #plt.show()

def run():
  small()
  medium()
  large()
  plt.show()

run()

#The function should display a small square using a line plot.
#The line should be a red dotted line with circle markers.
#The second function should be named medium and should have no parameters. 
#The function should display a medium square around the small square using a line plot.
#The line should be a green dashed line with square markers.
#The third function should be named large and should have no parameters.
#The function should display a large square around the medium square using a line  plot.
#The line should be a blue solid line with pentagon markers.