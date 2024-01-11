import helpers

while True:
  print("==== Contact List ====")
  print("1. Add contact")
  print("2. List all contacts")
  print("3. List favorites")
  print("4. Edit contact")
  print("5. Mark contact as favorite")
  print("6. Remove contact from favorite list")
  print("7. Remove contact")
  print("8. Exit")

  try:
    choice = int(input("What would you like to do? Type a number between 1 and 8: "))
    while choice < 1 or choice > 8:
        helpers.number_not_allowed(choice)
        choice = int(input("What would you like to do? Type a number between 1 and 8: "))

    if choice == "1":
       print("")
    elif choice == 8:
        break
  except ValueError:
      print("Oops! Invalid input. Please enter a number.")
