import helpers

contacts = []

def index():
  print("Contact List")
  
  for index, contact in enumerate(contacts, start=1):
    name = contact["name"]
    phone = contact["phone"]
    email = contact["email"]
    favorite = "✓" if contact["favorite"] else " "
    print(f"{index}. {name} - {helpers.phone_number_formatter(phone)}, {email} - Favorite [{favorite}]")
  return

def create():
  name = input("Type the contact name: ")
  phone = input("Type contact phone: ")
  email = input("Type contact email: ")
  favorite = input("Add to favorite list? Type 'Y' or 'N': " )
  is_favorite = False

  if favorite.upper() == "Y":
    is_favorite = True
    
  contact = {"name": name, "phone": phone, "email": email, "favorite": is_favorite}
   
  contacts.append(contact)
  return

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

    if choice == 1:
       create()
    if choice == 2:
       index()
    elif choice == 8:
        break
  except ValueError:
      print("Oops! Invalid input. Please enter a number.")
