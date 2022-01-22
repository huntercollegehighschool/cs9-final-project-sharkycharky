import replit

print("The teacher is very concerned because you won't explain why you were late and asks if you're okay. What will you do now? If you tell the teacher the truth, that you were just unmotivated to come to class, enter '1'. If you make up a lie about trains and show up to school on time from then on, enter '2'.")

choicea = input ("")

while choicea != '1' and choicea != '2':
  choicea = input("Please enter a valid input: ")

replit.clear()

if choicea == '1':
  import choice3b
elif choicea == '2':
  import choice1b