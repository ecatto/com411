def run():
  print("How many numbers should I sum up?")
  answer = int(input())

  count = 1
  total = 0

  while (count <= answer):
    print("please enter number {} of {}".format(count, answer))
    reply =int(input())
    total = total + reply
    count = count +1

  print("The total is", total)
