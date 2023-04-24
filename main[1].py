#Compatibility Test
print("Are you compatible with your partner?  Let's find out with this love score calculator!! ")

first_name = input("What is your name? \n")
second_name = input(" What is your partner's name?  \n")

name_combo = first_name + second_name
lower_case_letter = name_combo.lower()

t = lower_case_letter.count("t")
r = lower_case_letter.count("r")
u = lower_case_letter.count("u")
e = lower_case_letter.count("e")

true = t + r + u + e

l = lower_case_letter.count("l")
o = lower_case_letter.count("o")
v = lower_case_letter.count("v")
e = lower_case_letter.count("e")

love = l + o + v + e

compatibility_score = int(str(true) + str(love))

if compatibility_score < 10 or compatibility_score > 90:
  print(f"Your love score is {compatibility_score}, you go together like coke and mentos.")
elif compatibility_score >= 40 and  compatibility_score <=50 :
  print(f"Your love score is {compatibility_score}, you are alright together.")
else:
  print(f"Your love score is {compatibility_score}.")


 