def number_not_allowed(num):
  print("Choice not allowed. Choose another number.")

def phone_number_formatter(phone_number):
  digits_only = ''.join(filter(str.isdigit, str(phone_number)))

  if len(digits_only) != 11:
      return "Invalid phone number"

  formatted_number = f"({digits_only[:2]}) {digits_only[2]} {digits_only[3:7]}-{digits_only[7:]}"
  return formatted_number

def formatted_index(index):
   index = int(index) - 1
   return index

def formatted_contact(contact):
  favorite = "✓" if contact["favorite"] else " "
  print(f"{contact['name']} - {phone_number_formatter(contact['phone'])}, {contact['email']} - Favorite [{favorite}]")

  print(contact)

  