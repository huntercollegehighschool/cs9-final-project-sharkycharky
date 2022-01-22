import replit

print ("Well, now you have to actually find a group. How do you go about making friends after already having alienated your classmates? Since you've been so antisocial, if you give up and don't do the project at all, enter '1'. If you ask the closest person who also doesn't have a partner, enter '2'.")

friends = input ("")

while friends != '1' and friends != '2':
  friends = input("Please enter a valid input: ")

replit.clear()

if friends == '1':
  import choice3d
elif friends == '2':
  import choice3e