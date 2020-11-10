def cross_bridge(steps):
  for count in range (0,steps,1) :
    print("Crossed step")
  
  if steps>4 :
    print("The bridge is collapsing!")
  else:
    print("we must keep going!")

cross_bridge(3)
cross_bridge(6)

#The function should do the following
 #   Display the message "Crossed step" for each step crossed
  #  If the distance is more than 5 then the message "The bridge is collapsing!" should be displayed.
   # Otherwise the message "we must keep going!" should be displayed.

