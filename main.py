"""
Name(s): Charles Kirsch and Ashley Zhu
Name of Project: The Hunter Adventure
"""

import replit

print("You’re a Hunter student, arriving for your first day of class in seventh grade. You’ve just come from a public school in Brooklyn, and tested in because you’re basically a genius. However, you know nothing about how Hunter works or how you’re supposed to proceed. The administration keeps telling you that this will be a year of learning and decision making, and that will literally prove to be true. See if you can become a successful student by the end of the year by playing this game!")
print("If you want to arrive late to the first day, enter '1'. If you want to arrive on time, enter '2'.")

choice1 = input("")

replit.clear()

while choice1 != '1' and choice1 != '2':
  choice1 = input("Please enter a valid input: ")
if choice1 == '1':
  import choice1a
elif choice1 == '2':
  import choice1b
