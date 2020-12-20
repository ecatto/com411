import matplotlib.pyplot as plt

def small():
  plt.plot([3,4], [3,3], 'ro:')
  plt.plot([3,4], [4,4], 'ro:')
  plt.plot([3,3], [3,4], 'ro:')
  plt.plot([4,4], [3,4], 'ro:')
  #def small():
  #x = [3, 3, 4, 4, 3]
  #y = [3, 4, 4, 3, 3]
  #plt.plot(x, y, 'r:o')


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
