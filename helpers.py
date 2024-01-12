def number_not_allowed(num):
  print("Choice not allowed. Choose another number.")

def phone_number_formatter(phone_number):
  digits_only = ''.join(filter(str.isdigit, str(phone_number)))

  if len(digits_only) != 11:
      return "Invalid phone number"

  formatted_number = f"({digits_only[:2]}) {digits_only[2]} {digits_only[3:7]}-{digits_only[7:]}"
  return formatted_number