import matplotlib.pyplot as plt

def get_x():
  data=[18,21,20,21,23,17,16]
  #populate x value list using loop
  x=[]
  for count in range (len(data)):
    x.append(count)
  print(x)
  #populate x value list using range in len()
  x1 =range(len(data))
  print(x1)
  #put x and x1 into dictionary to show that range(0,7) is equivalent to x_list=[0,1,2,3,4,5,6]
  x_y ={}
  for count in range (7):
    x_y[x[count]]=x1[count]
  print(x_y)


def read_data(file):
  new_list = []
  with open(file) as file:
    for line in file:
      new_list.append(float(line.strip()))
  return new_list



def run_examples():
  data = read_data("visual/subplots/temps.txt")
  print(data)
  x=range(len(data))
  print(x)

  #2 ways of doing subplots -
  #method 1, 2 ways
  #method 1.1 Use fig,(ax1,ax2) = plt.subplots(a, b). a is how many rows. b is how many column. Eg (2,3) has 2 rows and 3 columns

  #method 1.1 Use fig,(ax1,ax2)= plt.subplots(a, b). label each subplot. ax1 is top left, ax2 next in sequence
  #fig, (ax1,ax2) = plt.subplots(2, 2)
  #ax1.plot(x,data)

  #method 1.2
  #indexes the name ofthe plot
  #when placing into grid, starts top left. [0,0] is top left, [0,1] is top right, [1,0] is bottom left and [1,1] is bottom right
  fig, axs = plt.subplots(2,2)
  axs[0,0].plot(x,data)


#fig, axes = plt.subplots(2, 2)
#  x1 = range(0, 10, 1)
#  y1 = range(0, 20, 2)
#  axs[0,0].plot(x1, y1)
#  axs[1,1].plot(x1, y1)
  plt.show()

def run():
  data = read_data("visual/subplots/temps.txt")
  print(data)
  x=range(len(data))
  print(x)
  fig,(plot1,plot2) = plt.subplots(1, 2)
  plot1.plot(x,data)
  plot1.set_ylim(0,25)
  #plot2.bar(x,data)
  
# OR....  
  #plt.subplot(121)
  #plt.plot(x,data)
  plotb = fig.add_subplot(122)
  plotb.bar(x,data)
  plt.show()

#get_x()
run()
