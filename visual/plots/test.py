import matplotlib.pyplot as plt

def display(x_value,y_value):
  plt.bar(x_value,y_value)
  plt.show()


def run():
  x_values =[ 1, 2, 3, 4, 5] 
  y_values =[1, 4, 9, 16, 25]
  #plt.bar(x_values,y_values)

  for count in range(5):
    plt.bar(count,y_values[count])
  plt.show()

run()
