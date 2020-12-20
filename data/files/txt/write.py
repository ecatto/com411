def search(file_name):
  print("Searching...", end="")
  sections = []
  books = []
  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):
        section = line.split(":")
        sections.append(section[1].strip())
      else :
        books.append(line.strip())
  print("Done!")
  return (sections,books)


def save(file_name,data_tup):
  print("Saving...")
  with open(file_name,"w") as file:
    file.write(f"Sections: [{data_tup[0]}]\n")
    file.write(f"Books: [{data_tup[1]}]")
  print("Done")

def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/books2.txt",data)

run()