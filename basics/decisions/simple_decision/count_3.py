even_count = int(0)
odd_count =int(0)

for count in range (3):
  print("Please enter a whole number.")
  num_one =int(input())
  if (num_one %2 == 1):
    odd_count = odd_count +1
  else:
    even_count = even_count +1
  
  
print("There were {} even and {} odd numbers.".format(even_count, odd_count))