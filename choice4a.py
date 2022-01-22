import replit

print ("“You’ve been doing great in school so far! But mental health is just as important as academic and social health. How are you balancing sleep time with work time? If you get as much sleep as you can, considering your workload and the time you have to get up to commute, enter '1'. If you get distracted and that means the work takes longer and it’s harder to fall asleep afterwards, enter ‘2’.")

sleepy = input ("")

while sleepy != '1' and sleepy != '2' :
  sleeepy = input("Please enter a valid input: ")

replit.clear()

if sleepy == '1':
  import success

if sleepy == '2':
  import sleep
