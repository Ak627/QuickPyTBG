room = 1
print("You are in a strange room")
while True:
  if room == 1:
    print("Your have found yourself in the first room of this house, it looks like a dining room of some sorts but everything is dirty, your only option is to go East")
    choice = input()
    if choice == 'East':
      room = 2
    else:
      print("Not an option")
  if room == 2:
    print("You walk to the second room of the house, a kitchen, different appliances are broken nothing works")
    print("You see a path South and back West")
    choice = input()
    if choice == 'South':
      room = 3
    elif choice == 'West':
      room = 1
    else:
      print("Not an option")
  if room == 3:
    print("Going down this part of the house you see pictures and find you're in the living room.")
    print("You see stairs leading down somewhere East and your path to the kitchen North")
    choice = input()
    if choice == "North":
      room = 2
    elif choice == "East":
      room = 4
    else:
      print("Not an option")
  if room == 4:
    print("You walk down the dusty stairs and into the basement, nothing seems to be in here except for the faint stench of mold and dust everywhere.")
    print("You can only go back up the stairs to the West.")
    choice = input()
    if choice == "West":
      room = 3
    else:
      print("Not an option")
