age = (input("Are you a cigarette addict older than 75 years old? ").lower() == "yes") 
chronic = (input("Do you have a severe chronic disease?").lower() == "yes")   
immune = (input("Is your immune system too weak?").lower() == "yes")
if age or chronic or immune:
  print("You are in risky group!")
else:
  print("You are not in risky group!")