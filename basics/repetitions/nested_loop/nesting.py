def run():
  print("Please enter a sequence of characters consisting of dashes and two markers")
  seq = input()

  print("Please enter the character for the marker")
  marker = input()
  print("")

  marker1 = -1
  marker2 = -1
  distance =0
  for count in range (0,len(seq),1):
    if seq[count] == marker :
      if marker1 == -1 :
        marker1 = count

      else:
        marker2 = count
        
  print("marker1 is", marker1)
  print("marker2 is", marker2)
  distance = (marker2-marker1)-1

  print("The distance between the markers is ", distance)