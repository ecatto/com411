def run():
  def listen():
    print("Please enter a word representing a sound")
    sound = input()
    print("That was a loud {}!".format(sound))

  listen()
