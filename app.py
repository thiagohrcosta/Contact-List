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

def list_favorites():
  favorite_contacts = []

  for contact in contacts:
     if contact["favorite"] == True:
        favorite_contacts.append(contact)
  
  print("Favorite contacts")

  for index, favorite_contact in enumerate(favorite_contacts, start=1):
     helpers.formatted_contact(index, favorite_contact)

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

def update():
   index()
   index_to_update = input("Type the contact index to update: ")
   formatted_index = helpers.formatted_index(index_to_update)

   contact = contacts[formatted_index]

   print("Contact to be edited")
   helpers.formatted_contact(formatted_index, contact)
   update_choice = update_user_choice()

   while update_choice > 0 and update_choice < 5:
      if update_choice == 1:
        contacts[formatted_index]["name"] = input("Type the new name: ")
        update_choice = update_user_choice()
      elif update_choice == 2:
        contacts[formatted_index]["phone"] = input("Type the new phone: ")
        update_choice = update_user_choice()
      elif update_choice == 3: 
        contacts[formatted_index]["email"] = input("Type the new email: ")
        update_choice = update_user_choice()
      elif update_choice == 4:
        is_favorite = input("Type 'Y' to mark as favorite or 'N' to remove from favorite: ")        
        contacts[formatted_index]["favorite"] = True if is_favorite.upper() == "Y" else False
        update_choice = update_user_choice()
      else:
        break
   return

def update_user_choice():
    update_choice = int(input("What would you like to edit (1 - Name  | 2 - Phone | 3 - Email | 4 - Favorite()? | 5 - Done : "))
    return update_choice
   
while True:
  print("==== Contact List ====")
  print("1. Add contact")
  print("2. List all contacts")
  print("3. List favorites")
  print("4. Edit contact")
  print("5. Remove contact")
  print("6. Exit")

  try:
    choice = int(input("What would you like to do? Type a number between 1 and 6: "))
    while choice < 1 or choice > 6:
        helpers.number_not_allowed(choice)
        choice = int(input("What would you like to do? Type a number between 1 and 6: "))

    if choice == 1:
       create()
    if choice == 2:
       index()
    if choice == 3:
       list_favorites()
    if choice == 4:
       update()
    elif choice >= 6:
        break
  except ValueError:
      print("Oops! Invalid input. Please enter a number.")
