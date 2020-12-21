#import matplotlib.pyplot as plt
import csv

def read_data():
  temperatures = {}
  with open("visual/subplots/temps.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    week1 =[]
    week2 =[]
    header = next(csv_reader)
    for row in csv_reader:
        print(f"{row[0]}:{row[1]}")
        week1.append(row[0])
        week2.append(row[1])
    print(week1)
    print(week2)

read_data()