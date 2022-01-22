import replit

print ("You’ve passed every hurdle so far! But now, it comes time for your first math test of the semester. How will you prepare for this challenge? If you will study for your math test a week in advance, using a study guide based on your notes, enter '1'. If you will try desperately to forget it exists until the night before and then frantically attempt to do a large amount of review in a little amount of time, enter '2'.")

choicele = input ("")

while choicele != '1' and choicele != '2' :
  choicele = input("Please enter a valid input: ")

replit.clear()

if choicele == '1':
  import choice4a

if choicele == '2':
  import choice3d
