def run():
  def display_ladder(steps):
    for count in range (steps):
      print("*****")
      print("*   *")
      print("*   *")


  def create_ladder():
    print("Please enter the number of steps")
    num_steps = int(input())

    display_ladder(num_steps)

  create_ladder()

