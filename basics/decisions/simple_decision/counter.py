def run():
  print("Please enter the first whole number.")
  num_one =int(input())
  print("Please enter the second whole number.")
  num_two =int(input())
  print("Please enter the third whole number.")
  num_three =int(input())

  even_count = int(0)
  odd_count =int(0)
  if (num_one %2 == 1):
    odd_count = odd_count +1
  else:
    even_count = even_count +1
  if (num_two %2 == 1):
    odd_count = odd_count +1
  else:
    even_count = even_count +1
  if (num_three %2 == 1):
    odd_count = odd_count +1
  else:
    even_count = even_count +1

  print("There were {} even and {} odd numbers.".format(even_count, odd_count))