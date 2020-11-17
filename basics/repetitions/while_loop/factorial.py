def run():
  print("Please enter a number:")
  answer = int(input())

  count =0
  total =1

  while (count <answer):
    count =count +1
    total = total *count

  print(total)