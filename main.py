import random
word_list=['apple','ball','cat','doll']

chosen_word=random.choice(word_list)
life = 5
display=[]
for _ in chosen_word:
  display+="_"
print(display)

while 1:

  a=input("Guess a letter").lower()

  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if (a==letter):
      display[position]=letter

  print(display)
  if a not in chosen_word:
    life -= 1
    print("You have", life, "lifes left")
  if '_' not in display:
    print("You Win")
    break
  if life==0:
    print("You Lose")
    break