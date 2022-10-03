# Password reminder
name = input("Please enter name: ").capitalize()
database = {
    "Razor" : "r4zor**123",
    "Eric"  : "£ric*",
    "John"  : "Starx4856",
    "Mithat2525" : "arif251625"
}

if name in database:
  print(f"Hello {name}! Your password: {database[name]}")
else:
  print(f"Hello {name}! See you later.")