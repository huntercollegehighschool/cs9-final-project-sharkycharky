import replit

print ("Since you happened to ask the only other un-partnered person in the class, they have essentially no choice but to work with you. How do you foster your one default friendship during this process? If you make the other person do all the work, act very hostile when they ask you to work, and then change everything at the last minute, enter ‘1’. If you act civilly, have a nice collaboration, and try to converse and bond as much as possible, enter ‘2’.")

collab = input ("")

while collab != '1' and collab != '2' :
  collab = input("Please enter a valid input: ")

replit.clear()

if collab == '1':
  import socialfail

if collab == '2':
 print ("Congratulations! You now have a healthy social life.")
 import choice2d
  
  
 