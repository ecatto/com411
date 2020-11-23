def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods), max(likelihoods))


def run():
  var = (likelihood())
  print("Minimum likelihood of falling: {}%".format(var[0]))
  print("Maximum likelihood of falling: {}%".format(var[1]))


run()
