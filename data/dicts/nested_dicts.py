def short_pattern():
  pattern ={"sequence":"101","occurrences":5}
  return pattern

def medium_pattern():
  pattern ={"sequence":"111000","occurrences": 25}
  return pattern

def long_pattern():
  pattern ={"sequence":"1100110011001100","occurrences":50}
  return pattern

def run():
  print("Analysing patterns...")
  full_dict ={"Short pattern":short_pattern(), "Medium pattern":medium_pattern(),"Long pattern":long_pattern()}

  for pair in full_dict:
    print(f"{pair} : {full_dict.get(pair)}")
  
  print("")
    
  for key, value in full_dict.items():
    print(f"{key} : {value}")


run()


#ALternative loop in run function
#for key, value in full_dict:
#    print(f"{key}:{value}")

#Finally, the function should display the content of the #dictionary as key-value pairs using an appropriate loop

#An example run of such a program is shown below:

#Analysing patterns...
#short sequence: {'sequence': '101', 'occurrences': 5}
#medium sequence: {'sequence': '111000', 'occurrences': 25}
#long sequence: {'sequence': '1100110011001100', 'occurrences': 50}