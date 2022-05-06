from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

def auction():
  answer = "no"
  biders = {}
  while answer == "no":
    user_name = input("What's your name?\n")
    bid = float(input("What's your bid? $\n"))
    biders[user_name] = bid
    answer = input("Are you the last of biders? (yes or no)\n")
    if answer == "no":
      clear()
    elif answer == "yes":
      answer = "yes"
    else:
      print ("Error, you must use lowercase and only 'yes' or 'no'!")

  value = 0.00
  for person in (0,len(biders) - 1):
    item = list(biders.keys())[person]
    user_value = biders.get(item)
  if user_value > value:
    value = user_value
    name_usr = item

  print(f"Winner is {name_usr} where bid is $ {value}")

auction()
