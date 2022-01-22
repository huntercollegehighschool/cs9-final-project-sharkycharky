import replit

print ("You have a group project, but since you don’t have any friends you’re not sure who to work with. What do you do? If you ask the teacher to work alone, enter '1'. If you lie and say you have a group, enter '2.' If you refuse to participate, enter '3'.")

choices = input ("")

while choices != '1' and choices != '2' and choices != '3':
  choices = input("Please enter a valid input: ")

replit.clear()

if choices == '1':
  print ("Oh no! You won't be allowed to work alone.")
  import choice3c
elif choices == '2':
 import choice3c
elif choices == '3':
 import choice3d
