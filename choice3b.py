import replit

print("The teacher tells you that consistently being late could impact your grade and asks if you will make an effort to come to class on time from then on. If you apologize for your lateness and say that you will, enter '1.' If you say no and stop coming to school at all, enter '2.'")

choiceb = input("")

while choiceb != '1' and choiceb != '2':
  choiceb = input("Please enter a valid input: ")

replit.clear()

if choiceb == '1':
  import choice1b
elif choiceb == '2':
  import fail
