def sum_weights(beep_weight,bop_weight):
  total_weight = beep_weight + bop_weight
  return total_weight

def calc_avg_weight(beep, bop):
  average = sum_weights(beep, bop)/2
  return average

def run():
  print("Please enter weight for beep")
  beep= int(input())
  print("Please enter weight for bop")
  bop = int(input())
  print("Would you like the total weight or the average weight? Please enter either sum or average")
  choice = input()

  if choice.lower() == "sum":
    print(sum_weights(beep, bop))
  elif choice.lower() == "average":
    print(calc_avg_weight(beep, bop))
  else:
    print("Please choose either sum or average")

# Run the program
run()