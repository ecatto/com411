def search(file_name):
  print("Searching...")
  with open(file_name) as file:
    for line in file:
      print(f"Looked in {line.strip()}")
  print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()
