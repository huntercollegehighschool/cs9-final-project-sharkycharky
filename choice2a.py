import replit

print("The teacher asks you why you were late to school. What do you do now? If you will make up an excuse, and then reform yourself and start being nicer to the teachers, enter '1.' If you will be sullen and withdrawn and not tell the teacher anything, enter '2.' If you will be incredibly rude and curse at the teacher because you don't care, enter '3.'")

choice = input("")

while choice != '1' and choice != '2' and choice != '3':
  choice = input("Please enter a valid input: ")

replit.clear()

if choice == '1':
  import choice1b
elif choice == '2':
  import choice2b
elif choice == '3':
  import choice3a