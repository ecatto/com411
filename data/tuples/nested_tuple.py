def steps():
  likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
  return likelihoods

def run():
  var = (steps())
  good_steps = []
  bad_steps = []
  for count in range (len(var)):
    if (var[count][1]>=50):
<<<<<<< HEAD
      bad_steps.append(var[count])
    else:
      good_steps.append(var[count])
=======
      good_steps.append(var[count])
    else:
      bad_steps.append(var[count])
>>>>>>> c7bd4c6022b71034b2d8ec94a068d6c19c386f5e

  print( "Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))

run()
