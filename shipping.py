weight = 4.8

# Ground Shipping
if weight <= 2:
  cost = weight * 1.5 + 20
  print("Ground Shippping $",cost)
elif weight >2 and weight <= 6:
    cost = weight * 3 + 20
    print("Ground Shippping $",cost)
elif weight > 6 and weight <=10:
    cost = weight * 4 + 20
    print("Ground Shippping $",cost)
elif weight > 10:
    cost = weight * 4.75 + 20
    print("Ground Shippping $",cost)

#Premium Ground Shipping
cost = 125
print("Ground Shipping Premium $",cost)

#Drone Shipping
if weight <= 2:
  cost = weight * 4.5
  print("Drone Shipping $",cost)
elif weight >2 and weight <= 6:
    cost = weight * 9
    print("Drone Shipping $",cost)
elif weight > 6 and weight <=10:
    cost = weight * 12
    print("Drone Shipping $",cost)
elif weight > 10:
    cost = weight * 14.25
    print("Drone Shipping $",cost)
