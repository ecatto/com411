def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)


def run():
  var = (likelihood())
  print("Minimum likelihood of falling: {}%".format(var))

run()

