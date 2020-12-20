def search(file_name):
  print("Searching...")
  data = {}
  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):
        section_name = (line.split(":")[1]).strip()
      elif (section_name in data):
        data[section_name].append(line.strip())
      else:
          data[section_name]=[line.strip()]
  print("Done!")
  return data

def run():
  data = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.csv","w") as file:
      for key,value in data.items():
        for book in value:
          file.write(f"{key}, {book}\n")

      #OR [file.write(f"{key}, {book}\n") for book in value]


run()
