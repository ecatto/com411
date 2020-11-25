def observed():
  observations = []
  for count in range (5):
    print("Please enter an observation")
    observations.append(input())
  return observations

def remove_observations(obs_list):
  is_running = True
  while (is_running == True) :

    print("Would you like to remove an observation?")
    reply = input()

    if reply == "yes":
      print("Please enter the observation to be removed")
      obs_list.remove(input())
    elif reply == "no":
      is_running = False
    else:
      print("please enter yes or no")

def run():
  var = observed()
  remove_observations(var)
  in_order =  set()

  for count in range(len(var)):
    tup = (var[count], var.count(var[count]))
    in_order.add(tup)

  print(var)
  for count in sorted(in_order):
    print(f"{count[0]} observed : {count[1]} times")

run()