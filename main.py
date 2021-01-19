import random
word_list=['apple','ball','cat','doll']

chosen_list=random.choice(word_list)

a=input("Guess a letter")

for i in chosen_list:
  if (a==i):
    print("right")

  else:
    print("wrong")
