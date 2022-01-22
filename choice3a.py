import replit

print ("You've been called to the principal's office because you cursed at a teacher. You are now at serious risk of suspension. The principal asks you what you will do to make up for your mistake. If you're so angry you curse at the principal too, enter ‘1.’ If you  apologize deeply and write “I’m sorry” 100 times in your notebook, enter ‘2’.")

choicec = input ("")

while choicec != '1' and choicec != '2' :
  choicec = input("Please enter a valid input: ")

replit.clear()

if choicec == '1':
  import fail
elif choicec == '2':
  import choice1b
