import random as rnd

def play_guess_the_number():

  print(rnd.randrange(1, 10, 1))

  print("Please enter the minimum value:")
  min = int(input())

  print("Please enter the maximum value:")
  max = int(input())

  random = (rnd.randrange(min, max, 1))

  print("I am thinking of a number between {} and {}.  Can you guess what it is?".format(min, max))
  guess = int(input())

  while guess != random:

    if guess < random:
      print("Your guess is too low")
    elif guess > random:
      print("Your guess is too high")
    print("Try again!")
    print("I am thinking of a number between {} and {}.  Can you guess what it is?".format(min, max))
    guess = int(input())

  print("Congratulations! You guessed my number!")

play_guess_the_number()
#Once you have the above program working as intended, you should turn it into a user-defined function name play_guess_the_number and call the function appropriately.