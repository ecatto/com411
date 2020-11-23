def directions():
  directions =["Move Forward","Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  direction = (directions())
  for count in range (len(direction)): 
    print("{} : {}".format(count,direction[count]))
  reply = int(input())
  return direction[reply]


def run():
  route =[]
  print("Working out escape route...")
  for count in range (5):
    route.append(menu())
  print("Escape route: {}".format(route))

run()