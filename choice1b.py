import replit

print("Congratulations! You’re down the path to success. Now, you face your next challenge; the first day. What do you do when you meet your peers? If you will tell them all about your life and say how happy you are to meet them and to be at Hunter, enter '1'. If you will be very stubborn and rude and tell them to mind their own business, enter '2'. If you will be shy and mysterious and not talk to anyone, enter '3'.")

choice3 = input("")

while choice3 != '1' and choice3 != '2' and choice3 != '3':
  choice3 = input("Please enter a valid input: ")

replit.clear()

if choice3 == '1':
  print ("You have a group project the next week and it goes wonderfully. You easily find people to work with, whom you cooperate with very well. Now you just have to prepare for your upcoming math test!")
  import choice2d
elif choice3 == '2':
  import choice2c
elif choice3 == '3':
  import choice2c



