import replit

print("You missed some of the lesson and now you can’t figure out what’s going on. What do you do next? If you will apologize for being late and ask the teacher for class notes, enter '1'. If you will choose inaction, enter '2'.")

choice2 = input("")

while choice2 != '1' and choice2 != '2':
  choice2 = input("Please enter a valid input: ")

replit.clear()

if choice2 == '1':
  print ("Excellent!")
  import choice1b
elif choice2 == '2':
  import choice2a
