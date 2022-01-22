import replit

print ("At this point, you’re not doing very well academically--in fact, your bad behavior has caused you to get bad grades in the first quarter. If you’re Hunter-student-smart about it, though, you can still turn things around. How do you proceed? If you will ask your teacher about extra-credit opportunities and make long study guides for every test and quiz, enter ‘1’. If you will brush the report card aside and play video games instead of concentrating as your grades continue to worsen, enter ‘2’.")

study = input ("")

while study != '1' and study != '2' :
  study = input("Please enter a valid input: ")

replit.clear()

if study == '1':
  import choice4a
elif study == '2':
  import fail