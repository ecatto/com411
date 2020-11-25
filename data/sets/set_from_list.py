def observed():
  observations = []
  for count in range (7):
    print("Please enter an observation")
    reply = input()
    observations.append(reply)

  return observations

def run():
  print("Counting observations...")
  var = observed()
  num_observed = set()
  for obs in var:
    tup = (obs, var.count(obs))
    num_observed.add(tup)

  for count in num_observed:
    print(f"{count[0]} observed : {count[1]} times")

run()

#    if (obs,count) in num_observed:
#      print("hi")
#      meh=obs
#      tup = (obs,count)
#      num_observed.remove(tup)
#      count=count+1
#      tup = (meh,(count))
#      num_observed.add(tup)
#    else:
#      print("boo")
#      tup = (obs,count)
#      num_observed.add(tup)


#  print(var)
#  print(num_observed)
